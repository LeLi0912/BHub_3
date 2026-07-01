"""领域分类器 — 将条目归入 7 个领域之一"""

import logging
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


def classify(item: Dict, fields: List[Dict]) -> str:
    """将单一条目分类到对应领域"""
    title = (item.get("title") or "").lower()
    abstract = (item.get("abstract") or "").lower()
    description = (item.get("description") or "").lower()
    text = f"{title} {abstract} {description}"

    best_field = None
    best_score = 0

    for field in fields:
        keywords = field.get("keywords", [])
        score = _score_text(text, keywords)
        if score > best_score:
            best_score = score
            best_field = field["id"]

    if best_field and best_score >= 1:
        return best_field

    return "other"


def _score_text(text: str, keywords: List[str]) -> int:
    """计算文本与关键词的匹配得分"""
    score = 0
    for kw in keywords:
        kw_lower = kw.lower()
        if kw_lower in text:
            # 精确短语匹配权重更高
            if " " in kw_lower:
                score += 3
            else:
                score += 1
    return score


def classify_all(items: List[Dict], fields: List[Dict]) -> List[Dict]:
    """批量分类"""
    for item in items:
        if "field" not in item:
            item["field"] = classify(item, fields)
    return items
