# Task Risk Gates

Use this file before deciding whether a request needs full project governance or a scoped edit. The goal is not to weaken discipline. The goal is to match governance cost to real risk.

## Contents

- Classification Algorithm
- Ordinary Engineering Task
- Lightweight Task
- Standard Task
- High-Risk Task
- Finding Severity Inside A Task
- Escalation Rules
- Output Format

## Classification Algorithm

1. Restate the user request in plain language.
2. Identify whether the request changes product behavior, data, permissions, runtime, deployment, or public-facing rules.
3. Check likely touched owners: docs, static assets, UI-only files, product code, API, database, auth, payment, provider adapter, config, deployment.
4. Classify as `普通工程任务`, `轻量任务`, `标准任务`, or `高风险任务`.
5. If uncertain, classify one level higher and explain the uncertainty.

Do not ask the user to choose the risk level. Recommend one classification and ask only for missing facts that would change the decision.

## Ordinary Engineering Task

Use `普通工程任务` when the task is a normal engineering execution request and does not need project governance:

- A clear bug fix with a known failing file, stack trace, test, compiler error, or reproducible symptom.
- A local UI tweak, component adjustment, CSS/layout fix, copy edit, or single-file change.
- A routine refactor, lint/type/test/build failure, dependency bump, or code review item.
- The owner file/module and validation path are clear enough to act without stage planning.

Procedure:

1. State briefly that this is a normal engineering task after skill-fit assessment.
2. Inspect only the relevant files and nearby owner pattern.
3. Make a narrow fix.
4. Run the targeted check, test, build, screenshot, or diff review that proves the change.
5. Report changed files, validation, and any `未验证` item.

Do not require project truth documents, current-stage implementation truth, broad audits, architecture reports, or user confirmation just because the skill is active.

Escalate out of `普通工程任务` if the task reveals missing owner boundaries, repeated AI fix loops, fake success, mock data, framework/SDK mismatch, or changes to schema, auth, permissions, payment, third-party providers, deployment, private material, release behavior, or user-facing acceptance.

## Lightweight Task

Use `轻量任务` when all are true:

- The task is docs-only, copy-only, static asset only, typo fix, README update, poster/image placement, or local visual/style adjustment.
- It does not change product logic, data model, permissions, payment, API contract, third-party integration, deployment, build system, secrets, or project architecture.
- It can be validated by inspecting the changed file, rendering/previewing when relevant, or running a small local command.

Procedure:

1. Read only the directly relevant files plus nearby conventions.
2. Check Git status and avoid overwriting unrelated user changes.
3. Make the smallest scoped edit.
4. Validate proportionally: file diff, markdown render, link/path check, screenshot, command, or targeted test when relevant.
5. Report changed files, evidence, and any `未验证` item.

Do not force current-stage implementation truth for lightweight tasks. In Chinese reports, say `轻量任务不强制实施真源，但仍需做范围内验证`. If the edit changes project rules or public install instructions, update README or compatibility notes as the truth surface for that change.

## Standard Task

Use `标准任务` when the request changes normal product behavior but stays inside existing architecture:

- Adds or modifies one clear user-facing behavior.
- Reuses an existing page, component, API route, service, model, or adapter.
- Does not introduce a new stack, schema model, auth model, permission model, payment lifecycle, deployment target, or third-party provider.

Procedure:

1. Run `/功能开工评估`.
2. Find current owner evidence.
3. Check whether the current-stage implementation truth already covers the task.
4. If covered and confirmed, execute one sub-stage.
5. If not covered, draft/update implementation truth and ask for confirmation before coding.

## High-Risk Task

Use `高风险任务` when any item is true:

- Changes stack, framework, SDK, package manager, directory ownership, build/deploy shape, or project skeleton.
- Changes database schema, migration, core fields, money, inventory, quota, irreversible status, or audit history.
- Changes auth, roles, permissions, data ownership, admin behavior, privacy, or security posture.
- Adds payment, membership, subscription, credits, quota, refunds, invoices, paid reports, or entitlement logic.
- Adds or changes a third-party API, SDK, OAuth, webhook, AI provider, storage, messaging, map, analytics, or platform service.
- Makes the project available to real users, clients, public URLs, production data, or external systems.

Procedure:

1. Run `/功能开工评估` and the specialized route such as `/第三方接入`, `/收费权益设计`, `/数据库设计`, `/后端架构`, `/接口安全`, `/部署路线`, or `/发布准备`.
2. Require source truth, official/provider docs when relevant, same-class evidence when useful, and explicit user confirmation.
3. Do not code until the foundation impact, chosen insertion route, rollback difficulty, validation method, and stop conditions are documented.

## Finding Severity Inside A Task

Risk class decides workflow cost. Finding severity decides what must be fixed now.

Classify important findings as:

- `阻断问题`: breaks the current goal, core user path, owner boundary, data truth, security/privacy, build/test baseline, or release path. Fix or get an explicit scope change before claiming progress.
- `设计风险`: may not break today, but creates architecture drift, duplicated owners, unbounded runtime behavior, weak validation, or future maintenance traps. Explain the tradeoff, record the validation entry, and ask before accepting the risk.
- `可记录债务`: does not affect the current goal or safety boundary. Record why it is safe to defer and where it should be handled later.
- `无关优化`: unrelated preference or broad cleanup. Do not attach it to the current task unless the user asks.

Do not use emotion or volume as severity. Evidence-free worries are not blockers. Evidence-backed blockers cannot be downgraded to "后面再说".

## Escalation Rules

Escalate from lightweight to standard if:

- A docs or UI change changes actual behavior, navigation, pricing, permissions, install command, or project rule.
- A "small bug" requires touching state, API, database, auth, provider calls, or build config.
- The changed file is generated, shared, or used by multiple product paths.

Escalate from standard to high-risk if:

- The feature needs a new data model, permission rule, provider, background job, webhook, or deployment setting.
- The current owner is unclear or there are multiple competing patterns.
- The user asks to "just change the framework/SDK" or "replace this whole part".

## Output Format

For every non-trivial request, state:

- Risk class.
- Why this class fits.
- What files or owners were checked or must be checked.
- Whether implementation truth is required.
- Important findings and their severity: `阻断问题`, `设计风险`, `可记录债务`, or `无关优化`.
- Validation evidence required.
- User decision needed, if any.

Invalid output:

- Asking the user to pick a risk class.
- Treating a high-risk task as lightweight because the code edit looks small.
- Blocking a pure README/copy/static-asset edit behind full product-stage planning.
- Expanding a normal bug fix, local UI tweak, single-file edit, or targeted test failure into a full project governance audit without evidence.
- Calling every concern a blocker, or downgrading a proven safety/data/owner problem into optional debt.
