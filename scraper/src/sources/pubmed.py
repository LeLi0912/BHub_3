"""PubMed E-utilities 采集模块"""

import logging
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional

import httpx

logger = logging.getLogger(__name__)

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch(
    queries: List[str],
    email: str = "",
    api_key: str = "",
    days_lookback: int = 7,
    max_per_query: int = 20,
    max_total: int = 100,
) -> List[Dict]:
    """从 PubMed API 获取论文列表"""
    if not email:
        logger.warning("PubMed: 未提供 email，NCBI 可能限制请求")

    all_pmids: List[str] = []
    with httpx.Client(timeout=30.0) as client:
        for query in queries:
            pmids = _search(client, query, email, api_key, max_per_query)
            all_pmids.extend(pmids)

        # 去重
        unique_pmids = list(dict.fromkeys(all_pmids))[:max_total]

        if not unique_pmids:
            return []

        items = _fetch_details(client, unique_pmids, email, api_key)
    logger.info("PubMed: 获取 %d 条详情", len(items))
    return items


def _search(
    client: httpx.Client,
    query: str,
    email: str,
    api_key: str,
    max_results: int,
) -> List[str]:
    params: Dict[str, str] = {
        "db": "pubmed",
        "term": query,
        "retmax": str(max_results),
        "retmode": "json",
        "sort": "date",
    }
    if email:
        params["email"] = email
    if api_key:
        params["api_key"] = api_key

    try:
        resp = client.get(ESEARCH_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        time.sleep(0.35 if not api_key else 0.1)
        return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        logger.warning("PubMed ESearch 失败: %s", e)
        return []


def _fetch_details(
    client: httpx.Client,
    pmids: List[str],
    email: str,
    api_key: str,
) -> List[Dict]:
    items: List[Dict] = []
    # NCBI 限制每次最多传 200 个 ID
    chunk_size = 200

    for i in range(0, len(pmids), chunk_size):
        chunk = pmids[i : i + chunk_size]
        params: Dict[str, str] = {
            "db": "pubmed",
            "id": ",".join(chunk),
            "retmode": "xml",
            "rettype": "abstract",
        }
        if email:
            params["email"] = email
        if api_key:
            params["api_key"] = api_key

        try:
            resp = client.get(EFETCH_URL, params=params)
            resp.raise_for_status()
            parsed = _parse_efetch_xml(resp.text)
            items.extend(parsed)
            time.sleep(0.35 if not api_key else 0.1)
        except Exception as e:
            logger.warning("PubMed EFetch 失败 (chunk %d): %s", i // chunk_size, e)

    return items


def _parse_efetch_xml(xml_text: str) -> List[Dict]:
    items: List[Dict] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        logger.warning("PubMed XML 解析失败: %s", e)
        return items

    for article_elem in root.iter("PubmedArticle"):
        try:
            item = _parse_article(article_elem)
            if item:
                items.append(item)
        except Exception as e:
            logger.debug("解析单条 PubMed 记录出错: %s", e)

    return items


def _parse_article(article_elem: ET.Element) -> Optional[Dict]:
    medline = article_elem.find(".//MedlineCitation")
    article = article_elem.find(".//Article")
    if medline is None or article is None:
        return None

    pmid_el = medline.find("PMID")
    pmid = pmid_el.text if pmid_el is not None else ""

    title_el = article.find("ArticleTitle")
    title = "".join(title_el.itertext()) if title_el is not None else ""

    abstract_el = article.find("Abstract/AbstractText")
    abstract = "".join(abstract_el.itertext()) if abstract_el is not None else ""

    # 作者
    authors = []
    author_list = article.find("AuthorList")
    if author_list is not None:
        for au in author_list.findall("Author"):
            last = au.find("LastName")
            fore = au.find("ForeName")
            if last is not None:
                name = f"{fore.text if fore is not None else ''} {last.text}"
                authors.append(name.strip())

    # 期刊
    journal_el = article.find("Journal/Title")
    journal = journal_el.text if journal_el is not None else ""

    # 日期
    pub_date = _parse_pub_date(article)

    # DOI
    doi = ""
    for eid in article_elem.iter("ELocationID"):
        if eid.get("EIdType") == "doi":
            doi = eid.text or ""
            break

    # 作者字符串
    author_str = ""
    if authors:
        if len(authors) <= 3:
            author_str = ", ".join(authors)
        else:
            author_str = f"{authors[0]}, {authors[1]}, {authors[2]} et al."

    return {
        "title": title.strip(),
        "authors": author_str,
        "link": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "doi": doi,
        "abstract": abstract.strip(),
        "published": pub_date,
        "source": "pubmed",
        "journal": journal,
        "pmid": pmid,
    }


def _parse_pub_date(article: ET.Element) -> Optional[datetime]:
    try:
        pd = article.find("Journal/JournalIssue/PubDate")
        if pd is None:
            return None
        year_str = pd.findtext("Year", "")
        month_str = pd.findtext("Month", "1")
        day_str = pd.findtext("Day", "1")
        month_str = month_str.replace("Jan", "1").replace("Feb", "2").replace("Mar", "3")
        month_str = month_str.replace("Apr", "4").replace("May", "5").replace("Jun", "6")
        month_str = month_str.replace("Jul", "7").replace("Aug", "8").replace("Sep", "9")
        month_str = month_str.replace("Oct", "10").replace("Nov", "11").replace("Dec", "12")
        year = int(year_str) if year_str else 2026
        month = int(month_str) if month_str else 1
        day = int(day_str) if day_str else 1
        return datetime(year, month, day, tzinfo=timezone.utc)
    except Exception:
        return None
