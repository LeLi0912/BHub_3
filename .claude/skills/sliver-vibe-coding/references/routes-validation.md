# Validation Routes

Use this file for stage validation, user acceptance, and quality gates.

## Contents

- `/阶段验收`
- `/用户验收陪跑`
- `/质量验收`

## `/阶段验收`

Goal: decide whether the current sub-stage or large stage is actually done.

Check:

- Requirements from current stage truth.
- Actual file changes.
- Extra work not in scope.
- Missing work.
- Tests, commands, UI evidence, API evidence, database evidence, logs.
- Security negative cases when applicable.
- Whether a Git checkpoint is ready.
- Whether bootstrap/adoption/stage guardrails pass when truth docs were created or changed.

Output:

- Passed items.
- Failed items.
- Unverified items.
- Evidence paths and command results.
- Guardrail result when applicable.
- Whether to update truth docs.
- Whether to commit.

Guardrail language:

- `项目结构门禁通过`: only means required truth files, headings, links, placeholders, and obvious drift markers passed.
- It does not prove code, UI, API, database, security, third-party, deployment, or user acceptance.

## `/用户验收陪跑`

Goal: translate technical validation into plain product checks the user can actually perform.

Use this when a non-technical user asks whether a feature is right, where to click, what to look at, or how to confirm acceptance.

Procedure:

1. Restate the feature as a user story.
2. Provide the shortest click path or API/request path, one step at a time.
3. For each step, state the expected visible result.
4. Include failure checks when relevant: empty input, wrong role, not logged in, canceled action, refresh, mobile size, provider failure, or slow network.
5. Tell the user exactly what screenshot, text, URL, or result to report.
6. Connect user-side checks with technical evidence already collected.

Output:

- What the user is validating.
- Click/check steps.
- Expected result per step.
- Failure signs.
- Evidence already verified by the agent.
- Open user-experience questions.

Invalid:

- Asking the user to read code, database rows, or logs as the primary acceptance method.
- Providing only test commands when the user needs product behavior.

## `/质量验收`

Goal: decide whether a feature, sub-stage, or stage is actually reliable enough for a non-technical user to trust. This is stricter than "it runs once".

Check:

- Source truth: requirement, stage truth, design/architecture docs, API/database/security docs.
- Task risk class from `task-risk-gates.md`; keep evidence proportional for lightweight tasks and strict for standard/high-risk tasks.
- Happy path: the intended user flow works end to end.
- Negative paths: invalid input, empty state, loading state, error state, canceled action, retry when relevant.
- Role/permission paths: not logged in, wrong role, own-data only, admin path when relevant.
- Data effects: database before/after, created/updated/deleted records, status changes, money/inventory/quota changes, transaction behavior.
- UI evidence: screenshot, responsive/mobile check, visible state, no obvious overlap or broken layout when relevant.
- API evidence: request/response examples, status codes, error shape when relevant.
- Third-party evidence: official docs checked, sandbox/API call, webhook/callback, failure behavior, redacted logs when relevant.
- Regression evidence: existing core flow still works or unverified regression risk is stated.
- Security/privacy basics: no secret leaks, sensitive logs redacted, input trust checked where relevant.
- Git readiness: changed files, ignored files, private files, checkpoint decision.
- Project guardrail readiness when governance artifacts changed.

Output:

- Pass/fail/未验证 table.
- Evidence paths and commands.
- User-visible result.
- Data/security result.
- Regression risk.
- What must be fixed before continuing.
- What can safely wait.
- Whether to update truth docs.
- Whether a Git checkpoint is ready.

Split the verdict by evidence plane:

- `结构门禁`: project truth/guardrail scripts.
- `代码门禁`: lint, type, unit, build, or framework checks.
- `合同链路`: API/protocol/schema/third-party contract evidence.
- `UI/用户侧`: screenshot, click path, visible behavior, acceptance questions.
- `数据/安全`: database effects, permissions, secrets, negative cases.
- `发布级`: deployment route, rollback, monitoring, cost, production settings.

Quality validation is invalid if it only reports tests passed without user-visible evidence and negative cases, or if it ignores data/security effects for features that touch backend, database, auth, permissions, payment, files, or third-party services.
