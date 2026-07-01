# GenoWeekly

每周生物信息学资讯汇总 — 工具更新、新方法论文、前沿进展。

## 项目概述

GenoWeekly 是一个自动化 + 人工审核的每周生信简报系统，由两部分组成：

- **Jekyll 前端** — 基于 GitHub Pages 的静态站点，展示每周内容
- **Python 爬虫** — 多源数据采集、分类、渲染，生成草稿供人工编辑

数据来源覆盖 BioRxiv、PubMed 和 GitHub Trending，内容归入基因组学、转录组学、单细胞组学、蛋白质组学、表观遗传学、宏基因组学、时空组学 7 个领域。

## 项目结构

```
.
├── _config.yml              # Jekyll 站点配置
├── _layouts/                 # Jekyll 布局模板
│   ├── default.html          #   基础 HTML 框架
│   ├── home.html             #   首页（最新一期内容）
│   ├── week.html             #   单期详情页
│   └── archive.html          #   归档列表页
├── _posts/                   # 每周正式内容（Markdown）
├── assets/css/
│   └── main.css              # 全部样式（白+灰+橙色调）
├── _preview.html             # 独立 HTML 预览（无需 Jekyll）
├── index.html                # 首页
├── about.html                # 关于页面
├── archive.html              # 归档页面
├── Gemfile                   # Ruby 依赖
│
├── scraper/                  # Python 爬虫
│   ├── pyproject.toml        #   uv 项目配置
│   ├── src/
│   │   ├── main.py           #   入口：协调爬取→分类→去重→渲染
│   │   ├── sources/
│   │   │   ├── biorxiv.py    #   BioRxiv RSS 采集
│   │   │   ├── pubmed.py     #   PubMed E-utilities 采集
│   │   │   └── github.py     #   GitHub Trending 采集
│   │   ├── classifier.py     #   领域分类器
│   │   ├── dedup.py          #   跨源去重
│   │   └── renderer.py       #   Markdown 渲染器
│   ├── config/
│   │   ├── fields.yaml       #   7 领域定义与关键词
│   │   ├── sources.yaml      #   数据源参数
│   │   └── pubmed_queries.yaml
│   └── output/               #   爬虫生成的草稿
│
└── docs/
    ├── architecture.md       # 系统架构文档
    ├── workflow.md           # 发布工作流
    └── content-spec.md       # 内容格式规范
```

## 前置条件

- **Python 3.12+** + [uv](https://docs.astral.sh/uv/)（爬虫）
- **Ruby** + Bundler（Jekyll 本地构建，可选）
- **Git**（推送部署）

## 快速开始

### 1. 初始化爬虫环境

```bash
uv sync --project scraper
```

### 2. 运行爬虫生成草稿

```bash
uv run --project scraper python src/main.py
```

选项：

| 参数 | 说明 |
|------|------|
| `--fetch-only` | 仅抓取不渲染 |
| `--source biorxiv/pubmed/github` | 仅抓取指定数据源 |
| `--output <path>` | 指定输出路径 |
| `--week N --year Y` | 指定周数/年份 |
| `-v` | 详细日志 |

### 3. 编辑并发布

编辑 `scraper/output/` 下的草稿，确认无误后移入 `_posts/`，提交并推送：

```bash
cp scraper/output/2026-W27-preview.md _posts/2026-07-06-week-27.md
git add _posts/2026-07-06-week-27.md
git commit -m "weekly: GenoWeekly #27"
git push origin main
```

推送后 GitHub Actions 自动构建并部署到 GitHub Pages。

### 4. 本地预览

直接浏览器打开 `_preview.html` 即可预览 UI 效果，无需安装 Jekyll。

## 7 大分类领域

| 领域 | 英文 | 关键词示例 |
|------|------|-----------|
| 基因组学 | Genomics | genome assembly, variant, SNP, GWAS, pangenome |
| 转录组学 | Transcriptomics | RNA-seq, splicing, gene expression, RNA velocity |
| 单细胞组学 | Single-cell | scRNA-seq, scATAC-seq, cell atlas, trajectory |
| 蛋白质组学 | Proteomics | mass spec, protein interaction, AlphaFold, peptide |
| 表观遗传学 | Epigenomics | methylation, histone, chromatin, ATAC-seq, Hi-C |
| 宏基因组学 | Metagenomics | microbiome, 16S, metagenomic assembly, taxonomic |
| 时空组学 | Spatial-omics | spatial transcriptomics, MERFISH, Visium, Xenium |

## 发布流程

```
运行爬虫 → 审核编辑草稿 → 移入 _posts/ → git push → GitHub Actions 自动部署
```

每次发布前须人工审核：精简过长的描述、修正分类错误、删除低质量条目、补充前沿进展综述。

## 技术栈

### 前端
- **Jekyll** (GitHub Pages) — 静态站点生成
- **纯 CSS** — 白+灰+橙色调，响应式布局（桌面/平板/手机）
- **无 JavaScript 框架** — 少量原生 JS 实现领域切换

### 爬虫
- **Python 3.12** + **uv** — 项目与依赖管理
- **httpx** — HTTP 客户端
- **feedparser** — RSS 解析
- **BeautifulSoup4** — HTML 解析
- **PyYAML** — 配置管理

## 文档

- [系统架构](docs/architecture.md) — 架构设计与组件说明
- [发布工作流](docs/workflow.md) — 详细操作步骤与配置说明
- [内容格式规范](docs/content-spec.md) — 排版、交互、字段规范

## 许可

本项目源代码仅供个人学习和使用。
