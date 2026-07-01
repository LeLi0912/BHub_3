"""Markdown 渲染器 — 将结构化数据渲染为 Jekyll post Markdown"""

import logging
from datetime import datetime
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

FIELD_NAMES_CN = {
    "genomics": "基因组学",
    "transcriptomics": "转录组学",
    "single-cell": "单细胞组学",
    "proteomics": "蛋白质组学",
    "epigenomics": "表观遗传学",
    "metagenomics": "宏基因组学",
    "spatial-omics": "时空组学",
}

FIELD_ORDER = [
    "genomics",
    "transcriptomics",
    "single-cell",
    "proteomics",
    "epigenomics",
    "metagenomics",
    "spatial-omics",
]


def render(items: List[Dict], week: int, year: int, summary: str = "") -> str:
    """将结构化数据渲染为 Jekyll post Markdown"""
    date = _week_to_date(year, week)
    date_str = date.strftime("%Y-%m-%d")
    title = f"GenoWeekly #{week}"

    tools, papers = _split_items(items)
    sources = _collect_sources(items)
    sources_str = "\n".join(f"  - {s}" for s in sorted(sources))

    lines: List[str] = []
    lines.append("---")
    lines.append(f"layout: week")
    lines.append(f'title: "{title}"')
    lines.append(f"date: {date_str}")
    lines.append(f"week: {week}")
    lines.append(f"year: {year}")
    lines.append("sources:")
    lines.append(sources_str)
    if summary:
        lines.append(f'summary: "{summary}"')
    else:
        tool_count = len(tools)
        paper_count = len(papers)
        lines.append(f'summary: "本期覆盖 {tool_count} 条工具更新、{paper_count} 篇新方法论文"')
    lines.append("---")
    lines.append("")
    lines.append("## 🛠 新工具与数据库更新")
    lines.append("")

    # 工具表格按领域分组
    for fid in FIELD_ORDER:
        field_cn = FIELD_NAMES_CN.get(fid, fid)
        field_tools = [t for t in tools if t.get("field") == fid]
        lines.append(f"### {field_cn}")
        lines.append("")
        if field_tools:
            lines.append("| 工具名 | 领域 | 一句话描述 | 链接 |")
            lines.append("|--------|------|-----------|------|")
            for t in field_tools:
                desc = _truncate(t.get("description") or t.get("abstract", "") or "", 60)
                link = _format_link(t)
                name = t.get("title", "")
                field_label = _get_field_label(t.get("field"))
                lines.append(f"| {name} | {field_label} | {desc} | {link} |")
        else:
            lines.append("| 工具名 | 领域 | 一句话描述 | 链接 |")
            lines.append("|--------|------|-----------|------|")
            lines.append("| _暂无更新_ | — | — | — |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 📄 新方法与论文")
    lines.append("")

    # 论文表格按领域分组
    for fid in FIELD_ORDER:
        field_cn = FIELD_NAMES_CN.get(fid, fid)
        field_papers = [p for p in papers if p.get("field") == fid]
        lines.append(f"### {field_cn}")
        lines.append("")
        if field_papers:
            lines.append("| 标题 | 领域 | 摘要(≤50字) | 期刊 | 链接 |")
            lines.append("|------|------|------------|------|------|")
            for p in field_papers:
                abstract = _truncate(p.get("abstract", "") or "", 50)
                journal = p.get("journal", "")
                link = _format_link(p)
                name = p.get("title", "")
                field_label = _get_field_label(p.get("field"))
                lines.append(f"| {name} | {field_label} | {abstract} | {journal} | {link} |")
        else:
            lines.append("_暂无更新_")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 🔬 前沿进展综述")
    lines.append("")
    lines.append("（此部分由你手写或基于爬虫素材汇总编辑，无固定格式限制）")
    lines.append("")

    return "\n".join(lines)


def _split_items(items: List[Dict]) -> tuple:
    """将条目分为工具和论文两类"""
    tools = []
    papers = []
    for item in items:
        source = item.get("source", "")
        if source == "github":
            tools.append(item)
        else:
            # 判断是工具还是论文
            title = (item.get("title") or "").lower()
            abstract = (item.get("abstract") or "").lower()
            tool_keywords = {"tool", "software", "database", "pipeline", "package", "workflow"}
            text = f"{title} {abstract}"
            if any(kw in text for kw in tool_keywords):
                item["_type"] = "tool"
                tools.append(item)
            else:
                item["_type"] = "paper"
                papers.append(item)
    return tools, papers


def _collect_sources(items: List[Dict]) -> List[str]:
    sources = set()
    for item in items:
        s = item.get("source", "")
        if s:
            sources.add(s)
    return list(sources)


def _truncate(text: str, max_len: int) -> str:
    if not text:
        return ""
    text = text.replace("\n", " ").replace("|", "/")
    if len(text) > max_len:
        return text[:max_len].rstrip() + "…"
    return text


def _format_link(item: Dict) -> str:
    url = item.get("link", "")
    source = item.get("source", "")
    if not url:
        return "—"

    labels = {
        "biorxiv": "bioRxiv",
        "pubmed": "PubMed",
        "github": "GitHub",
    }
    label = labels.get(source, "链接")
    return f"[{label}]({url})"


def _get_field_label(field_id: Optional[str]) -> str:
    mapping = {
        "genomics": "基因组",
        "transcriptomics": "转录组",
        "single-cell": "单细胞",
        "proteomics": "蛋白质组",
        "epigenomics": "表观遗传",
        "metagenomics": "宏基因组",
        "spatial-omics": "时空组",
    }
    return mapping.get(field_id or "", "")


def _week_to_date(year: int, week: int) -> datetime:
    """根据 ISO 周数计算周一日期"""
    from datetime import date, timedelta
    jan4 = date(year, 1, 4)
    first_monday = jan4 - timedelta(days=jan4.weekday())
    monday = first_monday + timedelta(weeks=week - 1)
    return datetime(monday.year, monday.month, monday.day)
