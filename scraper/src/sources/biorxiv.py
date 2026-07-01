"""BioRxiv RSS 采集模块"""

import logging
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional

import feedparser
import httpx

logger = logging.getLogger(__name__)

BASE_URL = "https://connect.biorxiv.org/biorxiv_xml.php?subject={}"

CATEGORY_MAP = {
    "bioinformatics": "bioinformatics",
    "genomics": "genomics",
    "molecular_biology": "molecular biology",
}


def fetch(categories: List[str], days_lookback: int = 7, max_per_category: int = 50) -> List[Dict]:
    """从 BioRxiv RSS 获取论文列表"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_lookback)
    items: List[Dict] = []

    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        for cat in categories:
            url = BASE_URL.format(cat)
            cat_label = CATEGORY_MAP.get(cat, cat)
            try:
                resp = client.get(url)
                resp.raise_for_status()
            except httpx.RequestError as e:
                logger.warning("BioRxiv RSS 请求失败 [%s]: %s", cat, e)
                continue

            feed = feedparser.parse(resp.text)
            count = 0
            for entry in feed.entries:
                if count >= max_per_category:
                    break

                published = _parse_date(entry)
                if published and published < cutoff:
                    continue

                items.append({
                    "title": entry.get("title", "").strip(),
                    "authors": _format_authors(entry.get("authors", [])),
                    "link": entry.get("link", ""),
                    "doi": _extract_doi(entry),
                    "abstract": entry.get("summary", "").strip(),
                    "published": published,
                    "source": "biorxiv",
                    "category": cat_label,
                })
                count += 1

            logger.info("BioRxiv [%s]: 获取 %d 条", cat, count)

    return items


def _parse_date(entry) -> Optional[datetime]:
    for field in ("published_parsed", "updated_parsed"):
        tp = entry.get(field)
        if tp:
            try:
                from time import mktime
                return datetime.fromtimestamp(mktime(tp), tz=timezone.utc)
            except Exception:
                continue
    return None


def _format_authors(authors: List[Dict]) -> str:
    names = [a.get("name", "") for a in authors if a.get("name")]
    if not names:
        return ""
    if len(names) <= 3:
        return ", ".join(names)
    return f"{names[0]}, {names[1]}, {names[2]} et al."


def _extract_doi(entry) -> str:
    for link in entry.get("links", []):
        href = link.get("href", "")
        if "doi.org" in href:
            return href
    for id_ in ("doi", "prism_doi"):
        val = entry.get(id_)
        if val:
            return str(val)
    return ""
