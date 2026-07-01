---
name: sliver-vibe-coding
description: Use when non-technical users build, take over, rescue, plan, validate, hand off, or release AI-assisted projects; when truth documents, technical selection, architecture, payment, third-party, security, deployment, AGENTS.md, Git/privacy, user acceptance, delivery gates, or project guardrails are involved; or when ordinary engineering work needs a lightweight skill-fit assessment.
---

# Sliver Vibe Coding

## Core Contract

Use this skill as a project-governance layer for users who mostly interact with AI by asking questions, reading answers, and asking for changes. Do not assume the user can read code, evaluate architecture, or validate security by themselves.

This is not a deep engineering execution skill. It should first assess whether ordinary coding work needs project governance before expanding the task.

Always optimize for six outcomes:

1. Ask enough questions to understand the project, especially when the user has no technical background.
2. Turn decisions into project truth documents before coding.
3. Execute only the current stage, with clear boundaries and evidence.
4. Support existing projects at any stage by first auditing current truth; never say the skill only works from scratch.
5. Own the technical judgment for the user: do not ask them to evaluate code quality, architecture, security, deployment, or AI output correctness by themselves.
6. Materialize repeatable project truth with bundled templates and validate the resulting project with guardrail scripts when governance artifacts are created or changed.

Default to Chinese and plain language. If the user says they do not understand, restate in simpler terms before proceeding.

## Skill-Fit Assessment

When a request looks like ordinary engineering work, do a lightweight skill-fit assessment before choosing the workflow. The goal is to avoid both extremes: do not ignore the skill when hidden governance risk exists, and do not force full project governance onto a small fix.

Classify the request as one of:

- `普通工程任务`: normal bug fix, local UI tweak, single-file edit, routine refactor, lint/type/test/build fix, or code review where the owner and validation path are clear.
- `轻量任务`: docs/copy/static-asset/style-only work inside this skill's governance surface, or a small change where a non-technical user needs plain-language evidence.
- `标准任务`: feature or flow change that needs owner evidence, current-stage truth, or user confirmation.
- `高风险任务`: stack, schema, auth, payment, third-party, deployment, security, private data, release, or agent constitution work.

For `普通工程任务`, keep the skill's role minimal: state that this is a normal engineering task, inspect the relevant files, fix narrowly, run the relevant test/check, and report evidence. Do not require project truth documents, stage plans, broad audits, or user confirmations unless the assessment finds a governance risk.

Escalate into governance if the task touches:

- Non-technical project direction or acceptance.
- Missing/stale/conflicting truth documents.
- Ownership or architecture uncertainty.
- Database, auth, permissions, payment, third-party, security, deployment, or private material.
- Repeated AI fix loops, fake success, mock data, duplicate owners, or unclear startup/runtime baseline.

## Distilled Operating Model

This skill is a distilled project-building workflow for non-technical users. It should guide the user through product clarification, technical judgment, architecture, implementation, validation, and delivery as one coherent operating system.

The baseline sequence is:

1. Create or identify the project space, internal truth-doc root, and Git checkpoint rules.
2. Establish the local run baseline: install state, versions, env placeholders, start command, first visible proof, and known blockers.
3. Clarify project brief and function list.
4. Split complex functions and large stages.
5. Choose one technical route.
6. Establish project architecture and agent constitution.
7. Build or repair frontend, database, backend, and security foundations as needed.
8. Write the current large-stage implementation truth document.
9. Execute one sub-stage at a time, validate, update truth documents, and checkpoint.
10. Run quality, user acceptance, deployment-route, release, and operations gates before treating a project as usable outside local development.

Existing projects do not restart from step 1. They enter at the first missing, stale, or unstable point after a read-only audit.

## Decision Style For Non-Technical Users

Ask more questions, but do not overwhelm the user. Prefer one small group of 3-5 blocking questions at a time.

When giving a recommendation:

- Give one recommended route first.
- Explain in plain Chinese why it fits this project.
- Explain the risk of not doing it.
- Name the exact user decision needed.
- Mark unknowns as `待确认` or `未验证`.

Do not answer with vague choices such as "都可以", "看情况", or a menu of equal options. If several routes are possible, recommend one primary route and list rejected routes with reasons.

## Proactive Knowledge Sweep

Non-technical users will not know what to ask. Before recommending work or marking work done, actively scan the relevant risk lanes instead of waiting for the user to mention them:

- Product: user, core flow, MVP, non-goals, roles, acceptance, business value.
- Documentation: truth root, active docs, stale docs, decision log, implementation truth.
- Technical route: framework/SDK fit, official docs, AI familiarity, conventions, license, maintenance.
- Frontend: design direction, token truth, UI library, responsive behavior, accessibility basics, empty/loading/error states.
- Backend: responsibility boundary, request lifecycle, owner layers, API contract, auth, permissions, data ownership.
- Database: schema/migrations, relationships, status, money, soft delete, transactions, backup/recovery.
- Monetization: paid value, plan, order, subscription, entitlement, quota, refund/cancel/expiry, webhook truth, audit.
- Runtime/environment: install state, package manager, language/runtime version, `.env.example`, local services, ports, first-run command, startup proof.
- Security/privacy: secrets, logs, input trust, injection, password/admin rules, sensitive data, third-party data transfer.
- Quality: happy path, negative cases, role cases, regression, data side effects, visual evidence, command evidence.
- Git/delivery: repo root, `.gitignore`, private files, internal docs, agent constitution privacy, checkpoints.
- AI-generated debt: duplicate components, dead files, fake fallbacks, mock data, custom wrappers, dependency sprawl, inconsistent patterns, unexplained generated code.
- Release/operations: environment, build, deploy, migrations, rollback, monitoring/logs, cost/quota, domain, user data, support path.

If a lane is not relevant, say why briefly. If it is relevant but not checked, mark it `未验证`.

## Route First

1. Infer the workflow route from the user's natural-language intent. Do not require the user to type a slash command.
2. If the user gives a slash command, treat it as an explicit shortcut and follow that route.
3. Classify task weight before applying heavy gates: `轻量任务`, `标准任务`, or `高风险任务`. Use `references/task-risk-gates.md` when the task size is unclear.
4. For `轻量任务` such as README, copy, poster, typo, local style, or docs-only edits that do not affect product behavior, use a scoped read-edit-validate loop. Do not force current-stage implementation truth.
5. If the user has an existing project and the task is not clearly lightweight, start with `/接管项目` even if they ask for implementation.
6. If the user only has an idea, start with `/立项`.
7. If the project cannot be started or the start command is unknown, run `/环境启动` before feature work.
8. If the user reports an error, repeated failed fixes, or "AI keeps changing things but still broken", run `/报错救援`.
9. If the project was heavily AI-generated, has duplicate files, mysterious wrappers, mock/fake data, or inconsistent patterns, run `/AI债务体检` before adding more features.
10. If the user is about to start a standard or high-risk feature, run `/功能开工评估` before writing code.
11. If no current-stage implementation truth exists for a standard or high-risk feature, do not code. Audit feature size, propose or create the implementation truth document, and ask the user to confirm the requirements first.
12. If the feature involves membership, payment, subscription, paid credits, quota, paid reports, paid downloads, trial, refund, invoice, or access after payment, run `/收费权益设计` before implementation.
13. If an inherited project uses a weak, outdated, non-official, or mismatched framework, SDK, library, or stack, run `/技术选型` as a review and ask the user to choose keep, repair, partial replacement, or migration before changing foundation.
14. If the project will leave local development but the deployment target is not designed, run `/部署路线` before `/发布准备`.
15. If the user needs to personally confirm a feature, run `/用户验收陪跑` so validation becomes click paths, expected screens, and pass/fail questions rather than technical jargon.
16. If the current stage is unclear, do a read-only stage diagnosis before recommending the next command.
17. If implementation would affect technology stack, directory structure, database schema, authentication, permissions, payments, API contracts, deployment shape, or core data fields, stop and ask for an explicit decision before changing files.
18. If the context is too large, the user wants a new window, or another agent will continue, run `/上下文交接` and produce a copy-paste-ready handoff before more work.

For the full stage map, read `references/project-flow.md`.

## Automatic Routing

Slash commands are optional power-user shortcuts and internal workflow labels. Most users will describe what they want in normal language. Route those requests automatically and say what you are doing in plain Chinese.

Do not ask the user to type `/立项`, `/技术选型`, or any other slash command. Say, for example, "我先帮你做立项信息补齐" or "这个功能开工前需要先做功能开工评估".

Common automatic triggers:

- "我想做一个项目", "从零开始", "从零做", "我有个想法" -> `/立项`.
- "不知道下一步", "帮我体检项目", "现在该做什么", "项目整体看看" -> `/项目体检`.
- "跑不起来", "怎么启动", "本地打不开", "安装失败", "端口被占用", "环境变量怎么填" -> `/环境启动`.
- "报错了", "一直修不好", "又坏了", "AI 改来改去还是不行", "同一个错误反复出现" -> `/报错救援`.
- "AI 写乱了", "项目越来越乱", "好多重复文件", "不知道哪些代码有用", "都是 mock/假数据" -> `/AI债务体检`.
- "我接手了", "我接手了一个项目", "帮我看看这个项目", "项目已经写了一半" -> `/接管项目`.
- "资料很乱", "dev-docs 没有", "文档不知道放哪" -> `/整理开发资料`.
- "功能拆分", "拆大阶段", "阶段怎么拆", "项目阶段怎么分" -> `/拆分`.
- "帮我选技术栈", "用什么框架", "前端后端怎么选", "操作本机软件", "系统自动化", "低约束样式工具", "零散组件片段", "一种语言", "两个语言服务", "跨语言", "技术栈怎么定" -> `/技术选型`, after checking whether `/立项` or `/拆分` is missing.
- "改 README", "改文案", "换海报", "修错别字", "调整局部样式", "只改说明文档" -> classify as `轻量任务`; do a scoped edit and validation without forcing implementation truth.
- Ordinary engineering prompts such as "修这个 TypeScript 报错", "只改相关文件", "按钮颜色", "间距", "单测失败", "修一个单测", "这个函数有 bug", or "只改这个文件" -> run a lightweight skill-fit assessment. If no governance risk exists, proceed as `普通工程任务` with narrow engineering execution.
- "我要开始做", "我要开始做这个功能", "加一个模块", "改这个流程" -> `/功能开工评估`.
- "没有实施真源", "还没写阶段文档", "可以直接开发吗" -> `/阶段计划`, propose current-stage implementation truth before coding.
- "API", "SDK", "OAuth", "webhook", "第三方", "支付接口", "地图", "AI provider", "storage", "messaging", "analytics", "平台服务" -> `/第三方接入`.
- "会员付费", "付费会员", "会员订阅", "付费", "订阅", "积分", "额度", "收费", "价格", "退款", "发票", "试用", "解锁功能", "付费报告" -> `/收费权益设计`, then `/第三方接入` if a provider is involved.
- "页面很乱", "前端骨架", "UI 不统一", "组件怎么放" -> `/前端骨架`.
- "数据库怎么设计", "要不要建表", "字段怎么定", "迁移怎么做" -> `/数据库设计`.
- "后端要不要做", "API 怎么设计", "业务规则放哪" -> `/后端边界`.
- "后端架构怎么设计", "后端目录怎么分", "后端规则怎么定", "后端怎么分层" -> `/后端架构`.
- "后端骨架", "搭后端骨架", "最小后端骨架" -> `/后端骨架`.
- "骨架验收", "接口返回不统一", "目录结构乱" -> `/骨架验收`.
- "接口安不安全", "权限会不会乱", "权限设计", "输入校验安全吗" -> `/接口安全`.
- "配置安全", "密钥会不会泄露", "env 怎么放", "日志会不会泄露" -> `/配置安全`.
- "git", "没有 git", "初始化 git", "提交", "推 GitHub", "远程仓库", "配置远程地址", "只配置不要推送", "会不会泄露", "忽略文件", "内部资料不能推", "参考项目库", "回滚", "revert", "重置", "恢复到旧版本", "同一个 commit" -> `/git保护`.
- "生成 AGENTS.md" -> `/生成宪法`.
- "写宪法", "AGENTS.md", "这个宪法有用吗", "宪法有没有用" -> `/宪法体检`.
- "开始写代码", "继续实现" -> check current-stage truth and route to `/执行子阶段` only if confirmed.
- "我怎么确认", "我点哪里看", "这个功能对不对", "给我验收步骤" -> `/用户验收陪跑`.
- "阶段验收", "验收一下", "做完了吗", "能不能提交", "测试一下", "质量过了吗" -> `/阶段验收` or `/质量验收`.
- "部署到哪里", "用什么平台上线", "Vercel/Netlify/Render/Supabase 怎么选", "生产环境怎么设计" -> `/部署路线`.
- "上线", "部署", "发布", "给别人用", "交付客户", "生产环境" -> `/部署路线` if deployment route is missing, otherwise `/发布准备`.
- "换窗口", "新窗口继续", "交给另一个 AI", "给我一份交接", "上下文太长" -> `/上下文交接`.
- "感觉跑偏了", "需求变了", "和文档不一致" -> `/防漂移`.

## Workflow Route Labels

Use these route labels to load the right reference files. The labels are for agent coordination; the user does not need to know or type them. If the user writes a command-like phrase without the slash, treat it as the same command.

| Command | Purpose | Load |
| --- | --- | --- |
| `/任务风险分级` | Decide whether the request is lightweight, standard, or high-risk before applying governance cost. | `references/task-risk-gates.md` |
| `/项目体检` | Proactively audit project state across product, docs, stack, architecture, quality, security, Git, release, and choose the next safest route. | `references/project-intake.md`, `references/project-flow.md`, `references/routes-intake.md` |
| `/环境启动` | Establish or repair the local first-run baseline: dependencies, versions, env placeholders, services, ports, start command, and first visible proof. | `references/beginner-failure-modes.md`, `references/routes-rescue.md`, `references/git-and-delivery.md` |
| `/报错救援` | Rescue repeated errors with reproduction, classification, official-doc/upstream checks, first failing boundary, minimal fix, and proof. | `references/beginner-failure-modes.md`, `references/routes-rescue.md` |
| `/AI债务体检` | Audit AI-generated sprawl, duplicate code, fake data, custom wrappers, dependency sprawl, dead files, and unsafe shortcuts before more development. | `references/beginner-failure-modes.md`, `references/routes-rescue.md`, `references/security.md` |
| `/接管项目` | Audit an existing project and decide where this workflow can enter. | `references/project-intake.md`, `references/project-templates.md` |
| `/立项` | Clarify product, users, MVP, boundaries, data objects, and acceptance rules. | `references/routes-intake.md`, `references/question-bank.md`, `references/project-templates.md` |
| `/拆分` | Turn the project into a function list, complex-feature docs, and large stages. | `references/routes-intake.md`, `references/project-flow.md` |
| `/整理开发资料` | Audit missing, occupied, or messy internal development truth documents before reorganizing them. | `references/project-intake.md`, `references/project-flow.md` |
| `/技术选型` | Produce one recommended technical route that fits the real project while prioritizing AI-familiar, convention-heavy, documented, official, non-from-scratch frameworks and SDKs. | `references/tech-stack.md` |
| `/第三方接入` | Design or audit a feature that depends on a third-party API, SDK, webhook, OAuth, payment, map, AI, storage, messaging, analytics, or platform service. | `references/third-party-integration.md`, `references/security.md` |
| `/收费权益设计` | Design paid value, plans, entitlement truth, quota, orders/subscriptions, refunds/cancel/expiry, provider/webhook route, and validation before monetization code. | `references/monetization-and-entitlements.md`, `references/third-party-integration.md`, `references/security.md` |
| `/功能开工评估` | Before coding a standard or high-risk feature, decide whether it touches project foundation and choose the best insertion route. | `references/routes-feature.md`, `references/project-flow.md`, `references/task-risk-gates.md`, `references/tech-stack.md`, `references/question-bank.md` |
| `/git保护` | Establish Git checkpoints and remote/privacy boundaries. | `references/routes-git.md`, `references/git-and-delivery.md` |
| `/生成宪法` | Generate a project-specific agent constitution from the bundled base template after evidence mapping. | `references/routes-constitution.md`, `references/agent-constitution.md`, `references/agent-constitution-template.md` |
| `/宪法体检` | Audit an existing agent constitution for shallow template adaptation and missing project binding. | `references/routes-constitution.md`, `references/agent-constitution.md`, `references/agent-constitution-template.md` |
| `/前端骨架` | Define and validate design-first frontend style, token truth, framework, UI library, modules, components, and minimal runnable skeleton. | `references/frontend-skeleton.md` |
| `/数据库设计` | Derive business objects, relationships, schema/migrations, and database validation. | `references/database-design.md` |
| `/后端边界` | Decide whether backend is needed and define backend responsibilities, API, permissions, language, and framework. | `references/backend-boundary.md` |
| `/后端架构` | Define backend architecture truth before skeleton code: business boundary, request lifecycle, owner layers, framework-first rules, API/error/log/config/data/auth boundaries, and new-module placement. | `references/routes-backend.md`, `references/backend-boundary.md`, `references/backend-skeleton.md`, `references/security.md` |
| `/后端骨架` | Build or audit the minimal backend skeleton after architecture truth exists. | `references/backend-skeleton.md` |
| `/骨架验收` | Validate backend rules, directory responsibility, API response examples, runtime evidence, and framework reuse. | `references/routes-backend.md`, `references/backend-skeleton.md` |
| `/接口安全` | Check identity, permissions, input trust, ownership, password rules, injection, and over-defense. | `references/security.md` |
| `/配置安全` | Check secrets, env examples, logs, dependencies, and database operation safety. | `references/security.md` |
| `/阶段计划` | Write the implementation truth document for the current large stage only. | `references/project-flow.md`, `references/routes-feature.md` |
| `/执行子阶段` | Execute only one current sub-stage and stop for review. | `references/routes-feature.md`, `references/git-and-delivery.md`, `references/task-risk-gates.md` |
| `/阶段验收` | Compare implementation to the stage truth document and collect evidence. | `references/routes-validation.md`, `references/git-and-delivery.md` |
| `/用户验收陪跑` | Translate technical validation into plain user click paths, expected screens, pass/fail questions, and evidence capture. | `references/beginner-failure-modes.md`, `references/routes-validation.md` |
| `/质量验收` | Verify user-visible behavior, negative cases, data effects, regression, security basics, and evidence before calling work done. | `references/routes-validation.md`, `references/security.md`, `references/git-and-delivery.md`, `references/task-risk-gates.md` |
| `/部署路线` | Choose one deployment route for the real project before release, including platform fit, env/secrets, data, public/private exposure, rollback, monitoring, and cost. | `references/beginner-failure-modes.md`, `references/routes-release.md`, `references/tech-stack.md`, `references/security.md` |
| `/发布准备` | Prepare deployment/release with environment, secrets, build, migration, rollback, monitoring, costs, privacy, and handoff checks. | `references/routes-release.md`, `references/git-and-delivery.md`, `references/security.md` |
| `/上下文交接` | Produce a copy-paste-ready handoff with current truth, git state, validation evidence, drift warnings, and next safe commands. | `references/context-handoff.md`, `references/git-and-delivery.md`, `references/project-flow.md` |
| `/防漂移` | Detect divergence from truth documents and decide whether to update docs, revise plan, or stop. | `references/project-flow.md`, `references/routes-release.md` |

## Mandatory Intake Behavior

Ask more questions than a normal coding assistant would. The point is not to interrogate the user; it is to prevent the AI from inventing product, architecture, or data rules.

Before any recommendation, ensure these are known from user answers, project files, or existing docs:

- Who uses the project.
- What core action the first version must complete.
- What is explicitly out of scope now.
- Whether the project is a website, mini program, app, admin system, script, or backend API.
- Whether login, roles, payments, uploads, or sensitive data exist.
- What truth documents already exist.
- Whether the current project is new, half-built, or already in production.
- Whether the project can start locally, what the user sees after startup, and what error blocks them if it cannot.
- Whether there are reference products, same-class open-source projects, competitor flows, screenshots, or existing user materials that should shape decisions.

Use `references/question-bank.md` for stage-specific questions. If answers already exist in files, cite those files instead of asking again.

## Existing Project Rule

Every workflow must be insertable into an existing project.

For existing projects:

1. Read current files and docs first.
2. Identify the real repo boundary, Git status, package/framework files, existing docs, frontend/backend/database structure, and run/test commands.
3. Produce a "current truth" summary before recommending changes.
4. Map the project to the closest stage in `references/project-flow.md`.
5. Prefer repair, documentation, and owner-layer fixes over rewriting.
6. If the current stack, framework, SDK, or provider integration looks suboptimal, compare it against the project goal and current evidence before recommending change.
7. Do not switch stacks, replace SDKs, create compatibility shims, fallback layers, or broad rewrites unless the user explicitly approves after seeing the tradeoff.

## Truth Documents

Treat truth documents as the project's single source of direction. The preferred internal folder is `dev-docs/`, but follow the existing repo convention when one is present. If `dev-docs/` is absent, occupied by unrelated material, or already messy, run the development-docs audit in `references/project-intake.md` before creating, moving, or rewriting docs.

When materializing a new project or adoption truth surface, use `references/project-templates.md` and the bundled `assets/project-bootstrap/` or `assets/project-adoption/` templates as raw material. Do not copy templates without adapting them to project evidence.

Common truth documents:

- Project brief.
- Function list.
- Complex feature documents.
- Large stage plan.
- Technical selection document.
- Frontend architecture truth.
- Database schema or migration truth.
- Backend architecture implementation truth.
- Security boundary report.
- Current stage implementation truth.
- Agent constitution.
- Quality and test evidence.
- Runtime and first-run evidence.
- AI debt or cleanup notes when the project has been heavily agent-generated.
- User acceptance checklist.
- Deployment route decision.
- Release and operations notes.
- Risk register and decision log.

Chat decisions are not official until written back to the relevant truth document. If the user changes a requirement mid-stage, update the truth document before coding.

When running `/技术选型`, audit all known project-intake materials before recommending a stack. Do not choose from one chat summary when project brief, function list, complex-feature docs, stage plan, architecture notes, user constraints, existing code, or user-provided reference materials exist.

If `/技术选型` has no reliable project-intake material, do not produce a final stack. Ask the user to complete the minimum `/立项` facts first, then return to technical selection.

If a user wants to develop a standard or high-risk feature and no current-stage implementation truth exists, create a proposed truth document path and outline before coding. Development can start only after the user confirms the feature scope, non-goals, size classification, first sub-stage, and validation method. For lightweight docs/copy/static-asset/style-only tasks, use `references/task-risk-gates.md` and do not force a stage truth document unless the edit changes product behavior or project rules.

After creating or changing bootstrap/adoption/constitution/stage truth artifacts, run `scripts/check_project_guardrails.py <project-root>` with the appropriate mode when a local project path is available. Treat this as a structural guardrail, not a replacement for real validation.

Read `references/agent-constitution.md` when creating or revising an agent constitution.

When generating an agent constitution, do not merely paste the base template and summarize the current project. The constitution is valid only after the project evidence pack, template-clause mapping, owner map, and validation commands are explicit. The bundled base template is `references/agent-constitution-template.md`.

## Validation Standard

Never accept "done", "optimized", "basically complete", or "safe" as evidence.

A stage can only be marked done when the response includes the relevant evidence:

- File paths changed or inspected.
- Commands run and results.
- App URL, screenshots, or visible behavior for frontend work.
- API request and response examples for backend work.
- Database migration/schema evidence for data work.
- Logs or health check output for runtime work.
- Security negative cases, not only happy path.
- Git checkpoint status when a stage is complete.
- Release or deployment readiness when the work is meant for real users.
- Remaining risk, owner, and next action in plain Chinese.

If evidence is missing, mark the item `未验证`.

## Multi-Agent Use

When the environment supports subagents and the task can be split cleanly, use them for independent read-only audits, stage extraction, or validation. For coding, only split work when file ownership is disjoint. Do not let multiple agents rewrite the same truth document or code area in parallel.
