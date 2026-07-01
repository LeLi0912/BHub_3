# Project Flow

This reference is the full project map. Use it to decide where a new or existing project enters the workflow.

## Contents

- Main Sequence
- Project Space And Internal Truth Root
- Pre-Code Foundation Rule
- Stage Inputs And Outputs
- Large Project Decomposition
- Current-Stage Implementation Truth Standard
- Proactive Project Health Lanes
- Feature Entry And Foundation Impact Gate
- Task Risk Gate
- Same-Class Solution Scan
- Third-Party Documentation Gate
- Truth-Document Order
- Truth Root Selection
- Template Materialization
- Project Guardrail Check
- Existing Project Entry Algorithm
- Context Handoff
- Drift Control

## Main Sequence

1. Project space, `dev-docs`, template set, and Git checkpoint rules.
2. Runtime/startup baseline: package manager, versions, env placeholders, local services, start command, and first visible proof.
3. Project brief: product, users, core flow, MVP, boundaries.
4. Function list and large stages.
5. Single technical route.
6. Project architecture and agent constitution.
7. Frontend skeleton.
8. Database design.
9. Backend boundary.
10. Backend architecture truth.
11. Minimal backend skeleton.
12. Backend skeleton validation.
13. Security validation.
14. Current large-stage implementation truth document.
15. Task risk classification before feature execution.
16. Feature entry assessment for the next standard or high-risk feature.
17. Monetization/entitlement truth when the stage touches paid access.
18. Sub-stage execution.
19. User acceptance walkthrough and quality validation.
20. Stage validation, truth-doc update, AI debt check, and Git checkpoint.
21. Deployment-route decision before release.
22. Context handoff when the current window is too large or another agent will continue.
23. Release readiness and operations handoff when the project will be used by real users.

Do not treat this as a rigid from-zero checklist. Existing projects enter at the first missing or unstable point.

## Project Space And Internal Truth Root

For a new project, help the user create or choose a clear English project folder before coding. Avoid starting from a random desktop, downloads, chat-export, or mixed-material folder.

Use `dev-docs/` as the preferred internal development truth root when no better convention exists. Explain to non-technical users that this folder is the internal "rule repository" for AI and the project team.

Do not treat internal truth docs as public product documentation. Before remote push, check whether `dev-docs/`, business plans, real cases, and agent constitution should stay private.

If the user wants version history for internal documents but does not want them pushed publicly, use dual-repo management: keep the code repo at the project root, add the internal truth-doc root to the code repo's `.gitignore`, and initialize a separate local-only Git repo inside the truth-doc root after confirming the path.

Before the first commit, create or repair `.gitignore` so secrets, internal docs, private agent constitution files, generated artifacts, local uploads, database dumps, and third-party reference projects are not accidentally staged.

When a new project or adoption truth surface must be materialized, use `references/project-templates.md` and the bundled templates:

- `assets/project-bootstrap/` for empty or effectively empty projects.
- `assets/project-adoption/` for half-built, inherited, forked, or AI-generated projects.

Templates are raw material. They must be adapted to project evidence before they become truth.

## Pre-Code Foundation Rule

Before writing business features in a new project, the standard order is:

1. Project brief and function list.
2. Technical selection.
3. Project architecture.
4. Agent constitution.

Frontend, database, backend, and security foundations are then built or audited according to the product shape. Do not let the agent jump directly from a one-sentence idea to feature code.

## Stage Inputs And Outputs

| Stage | Required input | Output | Existing project insertion |
| --- | --- | --- | --- |
| Project space / Git | Idea or existing directory | Project directory, `dev-docs`, Git baseline, privacy rules | Audit current repo and create a checkpoint before changes. |
| Runtime/startup | Project directory or inherited code | First-run map, command map, env placeholder map, startup proof or blocker | Use when project cannot run or startup is unknown. |
| Project brief | Idea, users, scenarios | Brief, user journey, MVP, non-goals, same-class/reference notes, differentiation, long-term direction | Backfill from existing app behavior and user answers. |
| Function list / stages | Brief | Function list, complex feature docs, large stage plan | Reverse-map existing features into a list. |
| Technical route | Product form, scope, deployment needs | One recommended stack, rejected options, risks | Review current stack; if it mismatches, ask whether to keep, repair, partially replace, or migrate. |
| Architecture / constitution | Stack, framework norms, product truth | Architecture truth and agent constitution | Audit current code and docs before changing rules. |
| Frontend skeleton | Design direction, style route, token truth, UI library, page flow | Runnable frontend base, UI rules, and token-backed components | Consolidate existing pages; do not rewrite by default. |
| Database design | User flows, business objects, permissions | Schema/migrations, field rules, data validation | Add or repair migration/schema truth; do not drop/rebuild casually. |
| Backend boundary | Function list, database design, API needs | Backend responsibilities, API boundary, language/framework decision | Use before adding new backend features or fixing backend confusion. |
| Backend architecture truth | Backend boundary, selected framework, database design, security requirements | Request lifecycle, owner layer map, API/error/log/config/data/auth rules, new-module placement | Audit current backend architecture before changing structure. |
| Backend skeleton | Architecture truth and framework norms | Minimal service with startup, config, health check, DB, responses, errors, logs, auth entry | Turn into skeleton audit for existing backend. |
| Skeleton validation | Code and architecture truth | Validation report and runtime evidence pack | Strong insertion point when backend is hard to change. |
| Security | APIs, permissions, config, dependencies, DB operations | Security boundary table, permission table, test evidence | Repeat per interface and before release. |
| Stage implementation | Large stage plan and truth docs | Current-stage implementation truth, sub-stage report | Most common existing-project entry: plan the next stage from current state. |
| Task risk classification | User request and likely owners | `轻量任务`, `标准任务`, or `高风险任务` plus validation level | Use before deciding whether full implementation truth is required. |
| Feature entry assessment | Feature request, current truth docs, architecture, owner files | Foundation-impact table and recommended insertion route | Use before adding any standard or high-risk feature to an existing or partially built project. |
| Monetization / entitlement | Paid feature request, product scope, provider needs | Paid value, entitlement truth, lifecycle, provider/webhook route, validation | Use before payment, subscription, credits, quota, membership, paid reports, or refunds. |
| User acceptance walkthrough | Implemented feature and user-visible route | Click path, expected visible states, failure signs, evidence request | Use when the user needs to confirm behavior without reading code. |
| Quality validation | Implemented behavior, truth docs, run/test commands, UI/API/data evidence | Pass/fail/未验证 evidence table and fix list | Use before commit, handoff, release, or continuing after a risky change. |
| AI debt check | AI-heavy project, repeated prompts, duplicate or fake paths | Must-fix debt, schedulable debt, ignored debt, cleanup route | Use before adding features to a messy generated project. |
| Deployment route | Validated app, stack, data/provider needs, release target | One recommended deployment route and pre-release blockers | Use before `/发布准备` if deployment target is not designed. |
| Release readiness | Validated stage, deployment target, env/config, data, third-party, security | Release verdict, deployment steps, rollback, monitoring, owner handoff | Use before real users, client delivery, public production, or private beta. |
| Context handoff | Large context, unfinished stage, or another agent will continue | Copy-paste-ready handoff with git state, truth docs, validation, drift warnings, and next commands | Use before changing windows or handing the project to another agent. |

## Large Project Decomposition

For large projects, never ask the agent to implement the whole product at once.

Decompose in this order:

1. Product roles.
2. Core business flows.
3. Modules that support those flows.
4. Complex feature documents for state machines, permissions, payment, refunds, coupons, content review, or other rule-heavy areas.
5. Large stages that each deliver one meaningful flow.
6. Current-stage implementation truth for only the next large stage.

Large stages should be ordered by usable product value, not by technical component order alone. A stage such as "login only" is not a valid large stage unless the product itself is an authentication product.

## Current-Stage Implementation Truth Standard

Create one file per active large stage, normally under `dev-docs/stages/<stage-name>.md` unless the repo already has a better convention.

Required sections:

1. Stage goal.
2. Target user role and complete flow.
3. Source truth documents.
4. Same-class solution evidence from GitHub, official examples, mature open-source products, or comparable product references.
5. Reference comparison: what to learn, what not to copy, business-fit judgment, and how this project should exceed the reference.
6. Third-party integration evidence when the stage depends on an external API, SDK, webhook, OAuth, payment, platform, or cloud service.
7. Monetization/entitlement evidence when the stage touches paid access: paid value, plan, entitlement truth, lifecycle, provider/webhook route, refund/cancel/expiry, quota, and audit.
8. Scope.
9. Non-goals.
10. Sub-stage table.
11. Per-sub-stage done standard.
12. Per-sub-stage validation evidence.
13. Owner files or modules likely touched.
14. Feature entry assessment and chosen insertion route.
15. Feature-size audit and split recommendation.
16. User confirmation status.
17. Foundation-impact check.
18. Security, permission, and data requirements.
19. Stop conditions.
20. Git checkpoint rule.
21. Unverified items.

The document is ready for implementation only when a non-technical user can answer:

- What will be usable after this stage?
- What will not be touched?
- What is the next sub-stage?
- How will completion be proven?
- Which changes would require stopping and asking?
- Which existing owner or module is the best entry point, and what alternatives were rejected?
- Does this feature touch foundation, and what exact evidence proves the answer?
- Is this feature small, medium, large, complex, or outside the current stage?
- Did the user confirm the scope, non-goals, first sub-stage, and validation method?
- Which same-class references were checked, what was learned, what was rejected, and how this project will fit the user's business better?
- Which third-party official docs were checked, what version/date was recorded, what API boundary was chosen, and what remains unverified?
- If paid access exists, what entitlement truth owns access, what lifecycle states exist, and how payment/refund/cancel/expiry are verified?

## Proactive Project Health Lanes

When the current stage is unclear, audit these lanes before selecting the next route:

| Lane | What to check | Common next route |
| --- | --- | --- |
| Product | user, core flow, MVP, non-goals, acceptance | `/立项` or `/拆分` |
| Docs | truth root, active docs, stale/conflicting docs, current-stage truth | `/整理开发资料` or `/阶段计划` |
| Stack | framework/SDK fit, official docs, AI familiarity, conventions, license | `/技术选型` |
| Runtime/startup | package manager, versions, scripts, env placeholders, local services, ports, first visible proof | `/环境启动` |
| Frontend | style route, token truth, UI library, routing, components, responsive states | `/前端骨架` |
| Database | business objects, schema/migrations, relationships, transactions, backup | `/数据库设计` |
| Backend | responsibility boundary, architecture truth, skeleton, API contract | `/后端边界`, `/后端架构`, or `/后端骨架` |
| Security | auth, permission, ownership, input trust, secrets, logs, dependencies | `/接口安全` or `/配置安全` |
| Third-party | official docs, SDK/API route, sandbox, webhook, quota, billing | `/第三方接入` |
| Monetization | paid value, plan/order/subscription, entitlement, quota, refund/cancel/expiry, webhook truth | `/收费权益设计` |
| AI debt | duplicate code, mock data, custom wrappers, unused files, dependency sprawl, inconsistent patterns | `/AI债务体检` |
| User acceptance | click path, expected states, failure signs, user evidence request | `/用户验收陪跑` |
| Quality | happy path, negative cases, role cases, data effects, regression | `/质量验收` |
| Git/privacy | repo root, ignore policy, internal docs, secrets, checkpoint | `/git保护` |
| Deployment/release | platform route, env, build, deploy, migration, rollback, monitoring, cost, handoff | `/部署路线` then `/发布准备` |

Choose one primary next route after the audit. Do not ask the user to choose from the whole map.

## Feature Entry And Foundation Impact Gate

Before coding a standard or high-risk feature, run `/功能开工评估` unless the current-stage implementation truth already contains an equivalent assessment.

The goal is to avoid hidden foundation changes. A small user-facing feature can still change core architecture if it introduces new auth rules, new ownership rules, new data fields, new API contracts, new providers, or a new directory pattern.

If no current-stage implementation truth exists, the assessment must not continue into code. It must first classify feature size, propose the implementation truth document, and get user confirmation.

The assessment must choose one insertion route:

- Reuse an existing owner module.
- Extend an existing page/component/service/API.
- Add a sibling module that follows current conventions.
- Add a backend endpoint or service boundary.
- Add a schema/migration inside the current data model.
- Add a third-party adapter after official documentation review.
- Redesign foundation after user approval.
- Stop because owner evidence is missing or contradictory.

Prefer the smallest route that completes the user's business result while respecting current architecture. Do not create a parallel system because it is faster in the moment.

Stop and ask before coding when the route affects stack, framework, database model, auth model, permission model, payment or money flow, API contract, deployment, directory ownership, or core data semantics.

Also stop before coding when:

- The feature is `大功能`, `复杂功能`, or `超出当前阶段`.
- No implementation truth document exists.
- The proposed implementation truth has not been confirmed by the user.
- The feature size cannot be classified from current docs and user answers.

## Task Risk Gate

Use `task-risk-gates.md` before applying full feature governance when the request may be small. This prevents copy, README, poster, local style, or docs-only edits from being treated like database/auth/payment work.

Risk levels:

- `轻量任务`: docs, copy, static assets, typo, or local visual/style changes with no product logic, data, permission, API, deployment, or architecture impact.
- `标准任务`: normal product behavior inside an existing owner and architecture.
- `高风险任务`: stack, schema, auth, payment, third-party, deployment, security, irreversible data, or foundation changes.

Only `标准任务` and `高风险任务` require the full current-stage implementation truth path. `轻量任务` still requires file inspection, Git-status awareness, scoped validation, and a clear report.

## Same-Class Solution Scan

Before writing the current-stage implementation truth document, prefer checking same-class solutions when the stage belongs to a mature problem space.

Good sources:

- GitHub repositories with active maintenance and clear docs.
- Official framework examples.
- Mature open-source products in the same category.
- Public product flows or docs from comparable products.

The goal is not copying. The goal is to avoid blind invention, understand common boundaries, then design a better fit for this user's business.

Record:

- Source.
- Why it is comparable.
- Useful pattern.
- Risk or mismatch.
- What not to copy.
- Business adaptation.
- How this project should be simpler, clearer, safer, more focused, or more valuable.

If current search is unavailable, mark the reference scan `未验证` and either proceed with local evidence only or ask the user to provide references.

## Third-Party Documentation Gate

Any stage involving a third-party provider must run `/第三方接入` before implementation truth is final.

The implementation truth must record:

- Official docs source.
- Checked date.
- API or SDK version.
- Auth method.
- Required configuration.
- API boundary.
- Webhook/callback behavior.
- Error and retry handling.
- Rate limit or quota risk.
- Security and secret handling.
- Sandbox/test plan.

If official docs cannot be checked, mark the item `未验证` and do not present the integration as ready.

## Truth-Document Order

Prefer these files, adjusting names to local convention:

1. `dev-docs/project-brief.md`
2. `dev-docs/function-list.md`
3. `dev-docs/stage-plan.md`
4. `dev-docs/technical-selection.md`
5. `dev-docs/architecture.md`
6. `dev-docs/frontend-architecture.md`
7. `dev-docs/database-design.md`
8. `dev-docs/backend-boundary.md`
9. `dev-docs/backend-architecture.md`
10. `dev-docs/security-boundary.md`
11. `dev-docs/stages/<stage-name>.md`
12. `dev-docs/monetization.md`
13. `dev-docs/runtime.md`
14. `dev-docs/quality/<stage-or-feature-name>.md`
15. `dev-docs/acceptance/<feature-or-stage-name>.md`
16. `dev-docs/ai-debt.md`
17. `dev-docs/deployment-route.md`
18. `dev-docs/release/<release-name>.md`

Do not force these exact paths if the repo already has a clear convention.

## Truth Root Selection

`dev-docs/` is the preferred internal truth root only when it is absent or already used for internal development material.

If `dev-docs/` does not exist:

- Search for an existing internal-doc convention first.
- If none exists, propose `dev-docs/`.
- Create it only after user confirmation.

If `dev-docs/` exists but is not development material:

- Do not repurpose it.
- Treat it as occupied.
- Propose another internal truth root, such as `internal-dev-docs/` or `docs/internal/`, matching repo style.
- Record the decision in the truth index.

If docs are messy:

- Create a docs inventory first.
- Mark files active, stale, conflicting, duplicate, public, or unrelated.
- Build a truth index before moving files.
- Ask before archiving, moving, deleting, or rewriting.

## Template Materialization

Use templates only when they reduce ambiguity and create usable truth.

Rules:

- Empty projects use the bootstrap template set only after the project root and privacy/Git boundary are clear.
- Existing projects use the adoption template set only after a read-only audit. Do not treat a half-built repo as empty.
- Do not copy template text as final truth. Replace generic fields with current file paths, owners, commands, risks, and user decisions.
- If a field cannot be known from files or user answers, write `未验证` and ask the smallest blocking question.
- When generating `AGENTS.md`, still follow `agent-constitution.md`: evidence pack, owner map, clause mapping, validation command map, then final draft.
- If `dev-docs/` is missing, occupied, or messy, run the development-docs audit before creating template files.
- If the truth docs are private, decide whether to keep them out of the public code remote before the first push.

## Project Guardrail Check

After creating or changing bootstrap/adoption/constitution/stage truth, run the structural guardrail when a local project path is available:

```bash
python3 scripts/check_project_guardrails.py <project-root> --mode bootstrap
python3 scripts/check_project_guardrails.py <project-root> --mode adoption
python3 scripts/check_project_guardrails.py <project-root> --mode constitution
python3 scripts/check_project_guardrails.py <project-root> --mode stage --stage-file dev-docs/stages/<stage-name>.md
```

The guardrail checks required files, headings, links, placeholder fields, obvious drift markers, and suspicious private filenames. It does not prove that the implementation works, that the user approved the plan, or that security is safe.

If the guardrail fails:

- Fix missing structure before coding when the task depends on that truth.
- If the failure is intentional because the repo uses another convention, document the convention and pass `--truth-dir <dir>` only after user confirmation.
- Do not hide placeholder or empty-field failures by calling them "template style" in a real project.

## Existing Project Entry Algorithm

1. Inspect repo boundary, Git status, package files, framework files, docs, tests, run commands, env examples, and startup evidence.
2. Summarize what exists and what is missing.
3. If the project cannot start or startup is unknown, choose `/环境启动` before feature work.
4. Review whether the current stack, framework, SDK, and third-party integration route fit the project.
5. If the route is mismatched, run `/技术选型` review and ask the user to choose keep, repair, partial replacement, or migration.
6. Audit whether AI-generated debt blocks safe continuation.
7. Map the project to the earliest unstable stage.
8. Ask the user whether the goal is rescue, continue, audit, refactor, add a feature, validate quality, choose deployment, or prepare release.
9. Choose one next command.
10. Keep the first action read-only unless the user explicitly asked for implementation and the current truth is sufficient.

## Context Handoff

Run `/上下文交接` when:

- The conversation is too large and the user wants to continue in a new window.
- Another agent or teammate will continue the project.
- A stage is partially complete and continuing without a written handoff would rely on chat memory.
- Release, deployment, or customer handoff is being prepared.

Use `references/context-handoff.md`. The handoff must include current git state, latest commits, changed files, validation evidence, missing evidence, runtime state, active truth docs, drift warnings, and exact next safe commands.

## Drift Control

Use `/防漂移` when:

- The current plan disagrees with a truth document.
- The AI proposes extra features not in the current stage.
- A request affects stack, schema, permissions, payment, auth, directory architecture, or core data fields.
- A feature has no proven insertion route or silently changes foundation.
- A proposed feature quietly switches framework, SDK, provider library, or technology stack.
- Validation evidence contradicts claimed completion.

Handle drift by writing:

1. What changed.
2. Which truth document is affected.
3. Whether it touches foundation.
4. Options: reject, update truth document, redesign stage, or stop for user decision.
