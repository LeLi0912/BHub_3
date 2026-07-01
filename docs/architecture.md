# GenoWeekly — 系统架构文档

## 概述

GenoWeekly 是一个每周生物信息学资讯汇总的静态网站，部署于 GitHub Pages。
系统由两个独立部分组成：**Python 爬虫**（本地运行，生成内容）和 **Jekyll 前端**（静态站点渲染）。

---

## 系统架构图

```
┌─────────────────────────────────────────────────────────┐
│                    本地环境 (你的电脑)                      │
│                                                         │
│  ┌─────────────────────────────────────┐                │
│  │          Python 爬虫 (uv)            │                │
│  │                                     │                │
│  │  BioRxiv RSS ──────┐               │                │
│  │  PubMed API ───────┤  classifier    │                │
│  │  GitHub Trending ──┘       │        │                │
│  │                            ▼        │                │
│  │                     renderer.py ────┤─── _posts/ 目录 │
│  └─────────────────────────────────────┘                │
│                          │                              │
│                          ▼                              │
│                 你手动编辑/审核 .md 文件                    │
│                          │                              │
│                          ▼                              │
│                  git add + git push                      │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                   GitHub (远程)                          │
│                                                         │
│  ┌──────────────────┐    ┌──────────────────────────┐   │
│  │  GitHub Repo     │    │  GitHub Actions           │   │
│  │  (main branch)   │───▶│  → Jekyll Build          │   │
│  │                  │    │  → Deploy to Pages        │   │
│  └──────────────────┘    └──────────┬───────────────┘   │
│                                     │                   │
│                                     ▼                   │
│                          ┌──────────────────────┐       │
│                          │  github.io 静态站点   │       │
│                          │  (完全静态 HTML/CSS)  │       │
│                          └──────────────────────┘       │
└─────────────────────────────────────────────────────────┘
```

---

## 前端架构 (Jekyll + GitHub Pages)

### 关键设计决策（开发过程中确认）

| 决策 | 结论 | 理由 |
|------|------|------|
| 图表实现 | 纯 CSS（无 JS 图表库） | 简报风格无需复杂图表，加载更快 |
| 领域切换方式 | 侧边栏点击切换（>900px）→ 横向标签栏（<900px） | 保证桌面端浏览效率与移动端触控体验 |
| 空领域处理 | 显示灰色"暂无更新"卡片 + 细条分布图 | 保持布局完整，避免用户误以为数据缺失 |
| 领域卡片行为 | 有更新可点击跳转，无更新不可点击 | 明确交互边界，减少无效点击 |
| 本地预览 | `_preview.html`（自包含 HTML） | 绕过本机无 Ruby/Jekyll 的限制，浏览器直接打开即可审核 UI |

### 技术选型理由

| 决策 | 选择 | 理由 |
|------|------|------|
| 静态站点生成器 | Jekyll | GitHub Pages 原生支持，零配置部署 |
| 主题 | 自建轻量主题 | 精确控制学术简报风格（白+灰+橙） |
| 样式 | 纯 CSS (无框架) | 简报风格不需要复杂 UI 框架，加载快 |
| 部署 | GitHub Actions | push 到 main 自动构建并发布 |

### 目录结构说明

```
GenoWeekly/
├── _config.yml              # Jekyll 全局配置
│   ├── 站点名称、描述、URL
│   ├── 主题设置（颜色变量、布局选项）
│   └── 分页配置
│
├── _layouts/
│   ├── default.html         # 基础 HTML 框架（包含导航栏、页脚）
│   ├── home.html            # 首页（显示最新一期 + 领域卡片 + 分布图 + 侧边栏布局）
│   ├── week.html            # 单期内容页（表格渲染、前后期导航）
│   └── archive.html         # 归档页（按年分组）
│
├── assets/css/
│   └── main.css             # 全部样式（白+灰+橙色系）
│       ├── CSS 自定义属性（颜色 token）
│       ├── 表格样式（工具/论文模块）
│       ├── 领域卡片网格（7 领域介绍卡片）
│       ├── 领域分布图（纯 CSS 水平柱状图）
│       ├── 领域侧边栏 + 内容面板布局
│       ├── 响应式：<900px 侧边栏 → 横向标签栏
│       ├── 排版（serif 标题, sans-serif 正文）
│       └── 媒体查询（移动端适配）
│
├── _posts/                  # 每周内容（爬虫生成草稿，你审核后提交）
│   └── YYYY-MM-DD-week-XX.md
│
├── index.html               # 首页布局
├── archive.html             # 归档页面
├── about.html               # 关于页面（项目介绍、数据源说明）
├── Gemfile                  # Jekyll gem 依赖
├── Gemfile.lock
│
├── _preview.html            # 开发用：独立 HTML 预览文件
│                            # 无需 Jekyll/Ruby，浏览器直接打开
│                            # 包含所有页面（首页/归档/关于）及 JS 切换逻辑
│                            # 用于本地 UI 审核，不提交到 GitHub Pages
```

### Jekyll Post 文件格式

每期内容是一个 Markdown 文件，位于 `_posts/` 目录，命名规则：

```
_posts/YYYY-MM-DD-week-NN.md
```

示例：`_posts/2026-07-06-week-27.md`

文件头部包含 YAML front matter：

```yaml
---
layout: week
title: "GenoWeekly #27"
date: 2026-07-06
week: 27
year: 2026
sources:
  - biorxiv
  - pubmed
  - github
summary: "本期覆盖 12 条工具更新、8 篇新方法论文、3 项前沿进展"
---
```

---

## 爬虫架构 (Python + uv)

### 技术选型

| 模块 | 库 | 用途 |
|------|---|------|
| HTTP 请求 | `httpx` | 异步请求 BioRxiv RSS、GitHub Trending |
| XML/RSS 解析 | `feedparser` | 解析 BioRxiv RSS feed |
| PubMed API | `xml.etree` + `httpx` | NCBI E-utilities API 调用 |
| HTML 解析 | `beautifulsoup4` | 解析 GitHub Trending HTML |
| 配置管理 | `PyYAML` | 读取数据源配置、领域关键词 |
| 项目构建 | `uv` + `pyproject.toml` | Python 依赖管理 |

### Python 版本

Python 3.12，由 `uv` 自动管理。

### 爬虫模块设计

```
scraper/
├── pyproject.toml          # uv 项目配置
├── src/
│   ├── __init__.py
│   │
│   ├── main.py             # 入口：协调爬取→分类→渲染流程
│   │   └── run()           # 一键运行全部流程
│   │
│   ├── sources/
│   │   ├── __init__.py
│   │   ├── biorxiv.py      # BioRxiv 采集
│   │   │   └── fetch()     # 按分类获取最新论文列表
│   │   ├── pubmed.py       # PubMed 采集
│   │   │   └── fetch()     # 按关键词检索最近一周文章
│   │   └── github.py       # GitHub Trending 采集
│   │       └── fetch()     # 获取本周热门生信仓库
│   │
│   ├── classifier.py       # 领域分类器
│   │   └── classify()      # 将条目归入 7 个领域之一
│   │
│   ├── dedup.py            # 跨源去重
│   │   └── deduplicate()   # 检查标题/URL 相似度去除重复
│   │
│   └── renderer.py         # Markdown 渲染器
│       └── render()        # 将结构化数据渲染为 Jekyll post Markdown
│
├── config/
│   ├── fields.yaml         # 7 个领域的定义与关键词
│   ├── sources.yaml        # 数据源配置（URL、关键词、频率）
│   └── pubmed_queries.yaml # PubMed 检索策略
│
└── output/                 # 爬虫输出目录（生成的草稿文件）
    └── week-XX-preview.md  # 每周草稿
```

### 数据源详情

#### BioRSS (BioRxiv RSS)

- 采集 URL: `https://connect.biorxiv.org/biorxiv_xml.php?subject=` + 分类名
- 覆盖分类: bioinformatics, genomics, molecular biology, systems biology
- 采集频率: 每次运行抓取最近 7 天内容
- 解析字段: title, authors, abstract, link, date, category

#### PubMed E-utilities

- API: NCBI E-utilities (ESearch + EFetch)
- 检索策略: 按领域关键词组合搜索最近 7 天
- 频率限制: 每秒 3 请求（遵守 NCBI 规则），自动添加 `api_key` 参数
- 解析字段: title, authors, journal, pmid, doi, abstract, publication date

#### GitHub Trending

- 采集 URL: `https://github.com/trending?since=weekly`
- 筛选条件: 生物信息学相关仓库（通过话题标签和描述关键词）
- 解析字段: repo name, description, stars, url, topics

---

## 领域分类系统 (7 个领域)

爬虫抓取到的条目通过关键词匹配 + 简单规则归入以下 7 个领域：

| 领域 | 英文标识 | 关键词匹配示例 |
|------|----------|---------------|
| 基因组学 | genomics | genome, whole genome, assembly, variant, SNP, GWAS |
| 转录组学 | transcriptomics | transcriptome, RNA-seq, expression, splicing, isoform |
| 单细胞组学 | single-cell | single cell, scRNA-seq, scATAC-seq, cell type |
| 蛋白质组学 | proteomics | proteome, mass spec, protein interaction, proteomics |
| 表观遗传学 | epigenomics | epigenome, methylation, histone, chromatin, ChIP-seq |
| 宏基因组学 | metagenomics | metagenome, microbiome, 16S, shotgun metagenomic |
| 时空组学 | spatial-omics | spatial, spatial transcriptomics, MERFISH, Visium |

每条未被分类的条目归入 "其他" 类别，在渲染时标记为待人工处理。

---

## 发布工作流

### 每周流程

```
周一  09:00  运行爬虫: uv run python src/main.py
      ↓
     生成草稿 Markdown → output/week-XX-preview.md
      ↓
 你打开文件，逐板块编辑、删改、补充
      ↓
     审核无误后，将内容复制到 _posts/YYYY-MM-DD-week-NN.md
      ↓
     git add → git commit → git push
      ↓
     GitHub Actions 自动构建并部署
      ↓
     https://<你的用户名>.github.io/GenoWeekly/ 更新完成
```

### 关键设计原则

1. **人工审核不可跳过**：爬虫仅提供草稿，每一条内容发布前都经过你确认
2. **表格格式严格统一**：渲染器按固定模板输出，保证每周格式一致
3. **GitHub 即 CMS**：不需额外后台，Git 提交记录就是内容版本管理
4. **纯静态**：最终产物是 HTML 文件，无需服务器，天生高可用
