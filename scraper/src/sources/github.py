"""GitHub Trending 采集模块"""

import logging
import re
from datetime import datetime, timezone
from typing import List, Dict, Optional

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

TRENDING_URL = "https://github.com/trending?since=weekly"


def fetch(since: str = "weekly", max_repos: int = 15, topics_keywords: Optional[List[str]] = None) -> List[Dict]:
    """从 GitHub Trending 获取热门生信仓库"""
    keywords = set(topics_keywords or [])
    repos: List[Dict] = []

    url = f"https://github.com/trending?since={since}"

    try:
        with httpx.Client(timeout=30.0, follow_redirects=True) as client:
            resp = client.get(url, headers={"Accept": "text/html"})
            resp.raise_for_status()
    except httpx.RequestError as e:
        logger.warning("GitHub Trending 请求失败: %s", e)
        return repos

    soup = BeautifulSoup(resp.text, "lxml")
    articles = soup.select("article.Box-row")

    for article in articles:
        if len(repos) >= max_repos:
            break

        repo_info = _parse_article(article, keywords)
        if repo_info:
            repos.append(repo_info)

    logger.info("GitHub Trending: 获取 %d 条", len(repos))
    return repos


def _parse_article(article, keywords: set) -> Optional[Dict]:
    # 仓库名
    h2 = article.select_one("h2 a")
    if not h2:
        return None
    href = h2.get("href", "")
    repo_name = href.strip("/") if href else ""

    # 描述
    desc_el = article.select_one("p")
    description = desc_el.get_text(strip=True) if desc_el else ""

    # 编程语言
    lang_el = article.select_one("span[itemprop='programmingLanguage']")
    if not lang_el:
        lang_el = article.select_one(
            "span.tmp-mr-3.d-inline-block ~ span:not([class])"
        )
        if not lang_el:
            lang_el = article.select_one("span.d-inline-block.ml-0 span:last-child")
    language = lang_el.get_text(strip=True) if lang_el else ""

    # 总星标数
    stars = 0
    stars_link = article.select_one("a.Link--muted[href*='stargazers']")
    if stars_link:
        star_text = stars_link.get_text(strip=True).replace(",", "")
        try:
            stars = int(re.search(r"[\d]+", star_text).group())
        except (AttributeError, ValueError):
            stars = 0

    # 本周星标数
    today_stars_str = ""
    today_el = article.select_one("span.d-inline-block.float-sm-right")
    if today_el:
        today_stars_str = today_el.get_text(strip=True)

    # 筛选：必须匹配生信关键词
    all_text = f"{repo_name} {description} {language}".lower()
    if not keywords or any(kw.lower() in all_text for kw in keywords):
        repo_url = f"https://github.com/{repo_name}"
        return {
            "title": repo_name,
            "description": description,
            "link": repo_url,
            "language": language,
            "stars": stars,
            "today_stars": today_stars_str,
            "published": datetime.now(timezone.utc),
            "source": "github",
        }

    return None
