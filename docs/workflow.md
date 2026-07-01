# GenoWeekly — 完整操作流程

> 从爬虫采集到 GitHub Pages 部署的完整步骤。

---

## 一次完整的发布流程

### Step 0: 本地预览 UI（可选）

直接浏览器打开 `_preview.html` 即可预览前端样式，无需安装 Ruby/Jekyll。

```bash
# WSL
explorer.exe _preview.html
# 或手动双击 _preview.html
```

### Step 1: 激活环境

```bash
# 进入项目目录
cd /mnt/c/Users/13637/Desktop/project/claudecode/BioinfoHub_2

# 同步爬虫依赖（首次运行或依赖变更后执行）
/home/lile/software/miniconda3/bin/uv sync --project scraper
```

### Step 2: 运行爬虫生成草稿

```bash
/home/lile/software/miniconda3/bin/uv run --project scraper python src/main.py
```

爬虫自动完成：
1. 并行抓取 BioRxiv RSS、PubMed API、GitHub Trending
2. 自动分类到 7 个领域（基因组、转录组、单细胞、蛋白质组、表观遗传、宏基因组、时空组）
3. 跨源去重
4. 生成草稿到 `scraper/output/<年份>-W<周数>-preview.md`

**常用选项：**

| 参数 | 说明 |
|------|------|
| `--source biorxiv/pubmed/github` | 仅抓取指定数据源 |
| `--week N --year Y` | 指定周数/年份（默认自动检测） |
| `--output <路径>` | 指定输出路径（可直接输出到 _posts/） |
| `-v` | 详细日志 |
| `--fetch-only` | 仅抓取不渲染（调试用） |

示例：

```bash
# 指定输出到 _posts/，跳过复制步骤
/home/lile/software/miniconda3/bin/uv run --project scraper python src/main.py --output ../_posts/2026-07-14-week-28.md --week 28 --year 2026
```

### Step 3: 人工审核编辑

打开生成的草稿文件，逐条处理：

| 处理项 | 操作 |
|--------|------|
| 描述过长 | 精简到一行内 |
| 分类错误 | 调整到正确领域 |
| 重复条目 | 删除（自动去重已处理大部分） |
| 低质量/无关内容 | 删除 |
| 缺失重要内容 | 手动补充 |
| 前沿进展综述 | 基于爬虫素材自行撰写段落 |

### Step 4: 发布正式帖子

审核通过后，将草稿移到 `_posts/`：

```bash
cp scraper/output/2026-W28-preview.md _posts/2026-07-14-week-28.md
```

> 如果 Step 2 已用 `--output` 直接输出到 `_posts/`，则跳过此步。

### Step 5: 提交并推送部署

```bash
git add _posts/2026-07-14-week-28.md
git commit -m "weekly: GenoWeekly #28 — 2026-W28"
git push origin main
```

推送后 GitHub Actions 自动：
1. 构建 Jekyll 站点
2. 推送到 `gh-pages` 分支
3. GitHub Pages 自动更新

访问：https://leli0912.github.io/BHub_3/

---

## 首次使用配置

### 1. 爬虫依赖

```bash
cd /mnt/c/Users/13637/Desktop/project/claudecode/BioinfoHub_2
/home/lile/software/miniconda3/bin/uv sync --project scraper
```

### 2. PubMed API Key（可选，推荐）

编辑 `scraper/config/sources.yaml`，填入 NCBI API Key 以提高请求频率限制（无 Key 每秒最多 3 次，有 Key 每秒最多 10 次）：

```yaml
pubmed:
  api_key: "your_ncbi_api_key_here"
  email: "your_email@example.com"
```

注册地址：https://ncbi.nlm.nih.gov/account/

---

## 项目结构速览

```
.
├── _config.yml                # Jekyll 站点配置（url/baseurl）
├── _posts/                    # 每周正式内容（Markdown）
├── _layouts/                  # Jekyll 布局模板
├── assets/css/main.css        # 全部样式
├── _preview.html              # 独立 HTML 预览
├── Gemfile                    # Ruby 依赖
│
├── scraper/                   # Python 爬虫
│   ├── pyproject.toml         # uv 项目配置
│   ├── src/main.py            # 入口
│   ├── src/sources/           # 数据源采集
│   ├── src/classifier.py      # 领域分类
│   ├── src/dedup.py           # 跨源去重
│   ├── src/renderer.py        # Markdown 渲染
│   ├── config/                # 配置文件
│   └── output/                # 草稿输出
│
├── .github/workflows/deploy.yml  # GitHub Actions 部署
└── docs/                          # 文档
```

---

## 每周发布清单

- [ ] 运行爬虫生成草稿
- [ ] 审核编辑草稿（精简、分类、去劣）
- [ ] 移入 `_posts/` 目录
- [ ] `git add` / `git commit` / `git push`
- [ ] 确认 Actions 运行成功
- [ ] 确认 https://leli0912.github.io/BHub_3/ 更新

---

## 故障排除

### 爬虫报错

| 错误 | 原因 | 解决 |
|------|------|------|
| PubMed 429 | 频率超限 | 等待 1 分钟重试，或配置 API Key |
| BioRxiv 无结果 | 网络或 RSS 变更 | 检查网络，换个时间段重试 |
| GitHub Trending 解析失败 | 页面改版 | 检查 `scraper/src/sources/github.py` |

### 部署失败

- 查看 Actions 日志：GitHub 仓库 → Actions → 最新的 workflow run
- 构建失败通常与 Gemfile 版本有关，确保 `github-pages` gem 版本兼容
- 404 检查：Pages 设置中 Branch 是否为 `gh-pages` / `(root)`
