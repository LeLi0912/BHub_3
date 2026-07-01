"""跨源去重模块"""

import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


def deduplicate(items: List[Dict]) -> List[Dict]:
    """检查标题/链接相似度，去除重复条目"""
    seen_titles: set = set()
    seen_links: set = set()
    deduped: List[Dict] = []

    for item in items:
        title = _normalize(item.get("title", ""))
        link = item.get("link", "")

        is_dup = False
        # 标题相似度检查
        for seen in seen_titles:
            if _similarity(title, seen) > 0.8:
                is_dup = True
                break

        if not is_dup and link:
            link_normalized = link.rstrip("/").lower()
            if link_normalized in seen_links:
                is_dup = True

        if is_dup:
            logger.debug("去重移除: %s", item.get("title", ""))
            continue

        seen_titles.add(title)
        if link:
            seen_links.add(link.rstrip("/").lower())
        deduped.append(item)

    removed = len(items) - len(deduped)
    if removed:
        logger.info("去重: 移除 %d 条重复", removed)

    return deduped


def _normalize(text: str) -> str:
    """标准化标题文本"""
    text = text.lower().strip()
    # 移除标点
    for ch in ".,;:!?\"'()[]{}":
        text = text.replace(ch, "")
    # 合并空白
    return " ".join(text.split())


def _similarity(a: str, b: str) -> float:
    """简单的 Jaccard 相似度计算"""
    if not a or not b:
        return 0.0
    words_a = set(a.split())
    words_b = set(b.split())
    intersection = words_a & words_b
    union = words_a | words_b
    if not union:
        return 0.0
    return len(intersection) / len(union)
