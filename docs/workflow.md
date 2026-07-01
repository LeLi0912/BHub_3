# GenoWeekly — 发布工作流指南

## 完整发布流程（每周一）

### Step 0 (可选): 本地预览 UI

如果本地未安装 Ruby/Jekyll，可使用独立 HTML 文件预览效果：

```bash
# 直接浏览器打开 _preview.html
xdg-open _preview.html
# 或手动在文件管理器中双击 _preview.html
```

`_preview.html` 是一个自包含的 HTML 文件，合并了所有页面（首页/归档/关于）和 JS 逻辑，用于 UI 审核。它不从 `_posts/` 读取数据（数据已硬编码在 HTML 中），因此仅用于前端样式验证，不替代 Jekyll 构建。

### Step 1: 运行爬虫生成草稿

```bash
cd /mnt/c/Users/13637/Desktop/project/claudecode/BioinfoHub_2

# 激活 uv 虚拟环境并运行爬虫
/home/lile/software/miniconda3/bin/uv run python scraper/src/main.py
```

爬虫执行内容：
1. 并行抓取 BioRxiv RSS、PubMed API、GitHub Trending
2. 自动分类到 7 个领域（基因组、转录组、单细胞、蛋白质组、表观遗传、宏基因组、时空组）
3. 跨源去重
4. 生成草稿文件到 `scraper/output/week-XX-preview.md`

输出示例：`scraper/output/2026-W27-preview.md`

### Step 2: 人工编辑审核

打开生成的草稿文件，逐条检查并修改：

| 处理项 | 操作 |
|--------|------|
| 工具描述过长 | 精简到一行内 |
| 分类错误 | 调整到正确领域 |
| 重复条目 | 删除重复（自动去重已处理大部分） |
| 低质量/无关内容 | 删除 |
| 缺失重要内容 | 手动补充 |
| 前沿进展综述 | 基于爬虫素材自行撰写段落 |

### Step 3: 发布正式帖子

审核通过后，将内容移到 `_posts/` 目录：

```bash
# 将编辑好的内容复制为正式帖子
cp scraper/output/2026-W27-preview.md _posts/2026-07-06-week-27.md

# 记得将文件开头的 layout 改为 week
# 并补充 front matter 中的 summary 字段
```

### Step 4: 推送部署

```bash
git add _posts/2026-07-06-week-27.md
git commit -m "weekly: GenoWeekly #27 — 2026-W27"
git push origin main
```

GitHub Actions 自动：
1. 触发 Jekyll 构建
2. 将站点部署到 GitHub Pages
3. 访问 `https://<用户名>.github.io/GenoWeekly/` 查看效果

---

## 爬虫配置管理

### 首次使用配置

```bash
# 创建项目根目录
cd /mnt/c/Users/13637/Desktop/project/claudecode/BioinfoHub_2

# 初始化 Python 项目
/home/lile/software/miniconda3/bin/uv init scraper
```

### 数据源配置 (scraper/config/sources.yaml)

```yaml
biorxiv:
  categories:
    - bioinformatics
    - genomics
    - molecular_biology
  days_lookback: 7
  max_results_per_category: 50

pubmed:
  api_key: ""  # 可选，填入 NCBI API Key 可提高频率限制
  email: ""    # 必填，NCBI 要求提供邮箱
  queries:
    - "(bioinformatics[All] OR computational biology[All]) AND (tool[All] OR software[All] OR database[All])"
    - "(genomics[All] OR genome[All] OR "whole genome"[All]) AND (method[All] OR algorithm[All] OR pipeline[All])"
    # ... 更多按领域划分的检索词
  days_lookback: 7
  max_results_per_query: 20

github_trending:
  since: weekly
  max_repos: 15
  topics_keywords:
    - bioinformatics
    - genomics
    - computational-biology
    - single-cell
    - variant-calling
    # ... 更多生信相关话题
```

### PubMed API 说明

NCBI E-utilities 免费使用但有限制：
- **无 API Key**：每秒最多 3 请求，超出会被 IP 封禁
- **有 API Key**：每秒最多 10 请求
- 建议注册 NCBI API Key 并配置到 `sources.yaml`

注册地址：https://ncbi.nlm.nih.gov/account/

---

## 爬虫运行选项 (main.py 设计)

```bash
# 完整运行（所有源 + 分类 + 渲染）
uv run python src/main.py

# 仅抓取不渲染（调试用）
uv run python src/main.py --fetch-only

# 仅某个数据源
uv run python src/main.py --source biorxiv

# 指定输出位置
uv run python src/main.py --output ../_posts/2026-07-06-week-27.md

# 指定周数（默认自动检测当前周）
uv run python src/main.py --week 27
```

---

## 目录与文件变更清单

每次发布需要关注的文件：

| 文件 | 动作 | 说明 |
|------|------|------|
| `_posts/YYYY-MM-DD-week-NN.md` | **新建** | 本周内容 |
| `index.html` | 不动 | Jekyll 自动显示最新帖子 |
| `archive.html` | 不动 | Jekyll 自动更新 |
| `scraper/output/week-XX-preview.md` | 删除或保留 | 草稿文件，发布后可清理 |

不需要动：
- `_config.yml`（除非修改站点配置）
- `_layouts/` 中的模板（除非修改页面设计）
- `assets/css/main.css`（除非修改样式）
- `scraper/` 下的代码（除非修改爬虫逻辑）

---

## 故障排除

### 构建失败
- GitHub Pages 构建日志: 仓库 → Actions → 最新的 workflow run
- 常见原因: Gemfile 与 GitHub Pages 版本不兼容
- 解决方案: 确保 `Gemfile` 中的 `github-pages` gem 版本与 GitHub 当前版本一致

### 爬虫报错
- BioRxiv RSS 不可用: 检查网络连接，换个时间段重试
- PubMed API 429 错误: 超过频率限制，等待 1 分钟后重试，或配置 API Key
- GitHub Trending 改版: 检查 HTML 解析逻辑是否需要更新
