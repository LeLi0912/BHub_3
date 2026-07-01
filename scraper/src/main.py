"""GenoWeekly 爬虫入口 — 协调爬取→分类→去重→渲染流程"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

import yaml

from src.sources import biorxiv, pubmed, github
from src.classifier import classify_all
from src.dedup import deduplicate
from src.renderer import render

logger = logging.getLogger(__name__)

# scraper 目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUT_DIR = PROJECT_ROOT / "output"
POSTS_DIR = PROJECT_ROOT.parent / "_posts"


def load_config(name: str) -> dict:
    """加载 YAML 配置文件"""
    path = CONFIG_DIR / name
    if not path.exists():
        logger.error("配置文件不存在: %s", path)
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def get_current_week() -> tuple:
    """获取当前 ISO 周数和年份"""
    from datetime import date
    today = date.today()
    iso = today.isocalendar()
    return iso[0], iso[1]


def fetch_all(config: dict) -> List[Dict]:
    """并行抓取所有数据源"""
    all_items: List[Dict] = []

    biorxiv_cfg = config.get("biorxiv", {})
    pubmed_cfg = config.get("pubmed", {})
    github_cfg = config.get("github_trending", {})

    # BioRxiv
    logger.info("开始抓取 BioRxiv…")
    biorxiv_items = biorxiv.fetch(
        categories=biorxiv_cfg.get("categories", []),
        days_lookback=biorxiv_cfg.get("days_lookback", 7),
        max_per_category=biorxiv_cfg.get("max_results_per_category", 50),
    )
    all_items.extend(biorxiv_items)
    logger.info("BioRxiv 完成: %d 条", len(biorxiv_items))

    # PubMed
    queries_cfg = load_config("pubmed_queries.yaml")
    logger.info("开始抓取 PubMed…")
    pubmed_items = pubmed.fetch(
        queries=queries_cfg.get("queries", []),
        email=pubmed_cfg.get("email", ""),
        api_key=pubmed_cfg.get("api_key", ""),
        days_lookback=pubmed_cfg.get("days_lookback", 7),
        max_per_query=pubmed_cfg.get("max_results_per_query", 20),
        max_total=pubmed_cfg.get("max_total", 100),
    )
    all_items.extend(pubmed_items)
    logger.info("PubMed 完成: %d 条", len(pubmed_items))

    # GitHub Trending
    logger.info("开始抓取 GitHub Trending…")
    github_items = github.fetch(
        since=github_cfg.get("since", "weekly"),
        max_repos=github_cfg.get("max_repos", 15),
        topics_keywords=github_cfg.get("topics_keywords", []),
    )
    all_items.extend(github_items)
    logger.info("GitHub Trending 完成: %d 条", len(github_items))

    return all_items


def run(
    fetch_only: bool = False,
    source: Optional[str] = None,
    output: Optional[str] = None,
    week: Optional[int] = None,
    year: Optional[int] = None,
):
    """运行完整的爬虫流程"""
    config = load_config("sources.yaml")
    fields_cfg = load_config("fields.yaml")
    fields = fields_cfg.get("fields", [])

    # 确定周数
    if year is None or week is None:
        auto_year, auto_week = get_current_week()
        year = year or auto_year
        week = week or auto_week

    logger.info("GenoWeekly #%d (第 %d 周, %d 年)", week, week, year)

    # 步骤 1: 抓取
    all_items = fetch_all(config)

    if not all_items:
        logger.warning("未抓取到任何条目")
        # 仍然生成空模板
        _write_output(week, year, [], output)
        return

    if fetch_only:
        logger.info("抓取完成 (fetch-only 模式)，共 %d 条原始条目", len(all_items))
        return

    # 步骤 2: 分类
    logger.info("正在分类…")
    all_items = classify_all(all_items, fields)
    field_counts = _count_fields(all_items, fields)
    for fid, cnt in field_counts:
        cn_name = _get_field_cn(fid, fields)
        logger.info("  %s (%s): %d 条", cn_name, fid, cnt)

    # 步骤 3: 去重
    logger.info("正在去重…")
    all_items = deduplicate(all_items)
    logger.info("去重后剩余: %d 条", len(all_items))

    # 步骤 4: 渲染
    logger.info("正在渲染 Markdown…")
    _write_output(week, year, all_items, output)


def _write_output(week: int, year: int, items: List[Dict], output_path: Optional[str] = None):
    """渲染并写入输出文件"""
    markdown = render(items, week, year)

    if output_path:
        out = Path(output_path)
    else:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        out = OUTPUT_DIR / f"{year}-W{week:02d}-preview.md"

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(markdown)

    logger.info("输出文件: %s", out.resolve())
    logger.info("包含 %d 条工具/论文条目", len(items))


def _count_fields(items: List[Dict], fields: List[Dict]) -> List[tuple]:
    """统计各领域条目数"""
    counts: Dict[str, int] = {}
    for item in items:
        fid = item.get("field", "other")
        counts[fid] = counts.get(fid, 0) + 1
    # 按配置顺序排列
    result = []
    for f in fields:
        fid = f["id"]
        if fid in counts:
            result.append((fid, counts[fid]))
    if "other" in counts:
        result.append(("other", counts["other"]))
    return result


def _get_field_cn(field_id: str, fields: List[Dict]) -> str:
    for f in fields:
        if f["id"] == field_id:
            return f.get("name_cn", field_id)
    return field_id


def main():
    parser = argparse.ArgumentParser(description="GenoWeekly 爬虫 — 每周生物信息学资讯采集")
    parser.add_argument("--fetch-only", action="store_true", help="仅抓取不渲染")
    parser.add_argument("--source", choices=["biorxiv", "pubmed", "github"], help="仅抓取指定数据源")
    parser.add_argument("--output", help="指定输出文件路径")
    parser.add_argument("--week", type=int, help="指定周数（默认自动检测）")
    parser.add_argument("--year", type=int, help="指定年份（默认当前年）")
    parser.add_argument("-v", "--verbose", action="store_true", help="详细日志")
    args = parser.parse_args()

    setup_logging(args.verbose)

    try:
        run(
            fetch_only=args.fetch_only,
            source=args.source,
            output=args.output,
            week=args.week,
            year=args.year,
        )
    except KeyboardInterrupt:
        logger.info("用户中断")
        sys.exit(1)
    except Exception as e:
        logger.exception("运行失败: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
