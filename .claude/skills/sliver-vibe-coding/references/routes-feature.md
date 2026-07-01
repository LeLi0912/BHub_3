# Feature Routes

Use this file for standard or high-risk feature entry, stage planning, and sub-stage execution. For tiny docs/copy/static-asset tasks, classify with `task-risk-gates.md` first.

## Contents

- `/功能开工评估`
- `/阶段计划`
- `/执行子阶段`

## `/功能开工评估`

Goal: decide whether a requested feature can enter the current project safely, whether it touches foundation, and what the best insertion route is. Do not write code in this command.

Use this when the user says they are ready to start a feature, add a module, change a core flow, or continue development but the exact entry point is not proven.

Procedure:

1. Restate the feature in plain language: target user, trigger action, expected visible result, and what is not included.
2. Classify task weight with `task-risk-gates.md`. If it is `轻量任务`, use the lightweight loop and do not force this full route.
3. Read current truth documents, architecture notes, agent constitution, package/framework files, route/module structure, database/schema files, API files, auth/permission files, and nearby implementation patterns.
4. Locate the likely existing owner layer: page, component, state, API route, service, model, migration, permission rule, config, job, webhook, or third-party adapter.
5. Decide feature type: pure UI addition, existing module extension, new sibling module, backend/API extension, schema/data change, permission/security change, third-party integration, cross-cutting workflow, or foundation change.
6. Check whether a current-stage implementation truth document already exists and covers this feature.
7. Audit feature size before choosing the execution route.
8. Produce a foundation-impact table.
9. Compare possible insertion routes and choose one recommended route.
10. If the route involves a third-party service, run `/第三方接入` before finalizing the decision.
11. If the feature involves monetization, run `/收费权益设计` before finalizing the route.
12. If the feature belongs to a mature pattern, use same-class solution evidence before choosing the route.
13. If no implementation truth exists, propose the document path and write a draft outline instead of coding.
14. Ask the user to confirm scope, non-goals, size classification, first sub-stage, and validation method before execution.
15. If the chosen route changes foundation, stop and ask the user to approve the redesign path before coding.
16. Write or update the current-stage implementation truth before execution.

Owner-layer decision must answer:

- Who creates this concept.
- Who calls it.
- Who consumes it.
- Which file, module, schema, service, state store, adapter, or truth document is the single owner.
- Which layers are forbidden owners.
- Which existing pattern proves the chosen owner.
- Which validation gate would catch the old or expected failure.

Feature-size audit categories:

- `小功能`: one existing owner, no schema/auth/API contract/foundation change, can be one sub-stage.
- `中功能`: touches two or more owners but still serves one clear user action; needs several sub-stages.
- `大功能`: completes a meaningful product flow, touches multiple modules or data rules; should become or update a current large-stage implementation truth.
- `复杂功能`: contains state machine, payment/refund, permission matrix, audit/review, third-party callback, irreversible status, or cross-role workflow; needs its own complex-feature document plus implementation truth.
- `超出当前阶段`: does not fit the current stage goal or non-goals; stop and ask whether to defer, split, or redesign the stage.

If no current-stage implementation truth exists for a standard or high-risk task:

- Do not run `/执行子阶段`.
- Do not edit product code.
- Propose the truth document path, normally `dev-docs/stages/<stage-or-feature-name>.md`, unless the repo has another convention.
- If the truth root is missing, occupied, or messy, run `/整理开发资料` first.
- Draft the minimum implementation truth outline with feature summary, size audit, scope, non-goals, owner evidence, insertion route, sub-stage split, done standards, validation, stop conditions, and open questions.
- Ask the user to confirm or correct the draft before coding.

Foundation-impact table must cover stack/framework, directory ownership, frontend route/state/component system, API contract, database/schema, auth/roles/permissions, payment/money/quota, third-party providers, deployment/env/secrets/jobs, logging/monitoring/privacy/security.

Output:

- Feature summary.
- Risk class and feature-size audit.
- Current owner evidence.
- Foundation-impact table.
- Recommended insertion route.
- Rejected routes and reasons.
- Proposed or existing implementation truth document path.
- Truth documents that must be updated.
- Required user decisions.
- First executable sub-stage and validation method.

The assessment is invalid if it only says "low risk" or "does not affect architecture" without file/doc evidence, skips feature-size audit, or starts coding before the user confirms the implementation truth.

## `/阶段计划`

Goal: write the implementation truth document for the current large stage only.

Procedure:

1. Read project brief, function list, stage plan, architecture truth, and relevant domain docs.
2. Prefer a same-class solution scan before designing the stage plan when the stage involves a common product or engineering pattern.
3. If any sub-stage depends on a third-party service, API, SDK, webhook, OAuth flow, payment provider, map provider, AI provider, storage provider, messaging provider, analytics provider, or platform capability, run `/第三方接入` before finalizing the implementation truth.
4. Run `/功能开工评估` for the first feature or risky feature in this stage before finalizing the implementation route.
5. Split the current large stage into sub-stages.
6. For each sub-stage, write what to do, done standard, validation method, files/modules likely involved, and what not to touch.
7. Ask the user to confirm the implementation truth before any `/执行子阶段`.
8. Do not implement yet.

Current-stage implementation truth document must include source truth, same-class evidence, third-party evidence when applicable, feature entry assessment, feature-size audit, user confirmation status, scope, non-goals, sub-stage table, done standards, validation methods, foundation-impact check, security/data notes, stop conditions, Git checkpoint rule, and unverified items.

Same-class solution evidence must include source name/link or local path, why comparable, useful pattern, what not to copy, license or reuse risk, business-fit differences, and how the current project should do better.

Do not copy source code, UI, content, brand, data, or product positioning from references. Use references to avoid blind design and raise the user's business outcome. If live GitHub/web search is unavailable, say so and mark the scan `未验证`, or ask the user for reference projects.

Implementation truth is invalid if it lacks non-goals, per-sub-stage done standards, validation methods, source truth, user confirmation when needed, feature-size audit, feature entry assessment, same-class scan decision, third-party official-doc evidence when applicable, or lets the agent continue automatically into the next sub-stage.

When the implementation truth file is created or substantially changed, run:

```bash
python3 scripts/check_project_guardrails.py <project-root> --mode stage --stage-file dev-docs/stages/<stage-name>.md
```

If the repo uses another truth path, pass that path with `--stage-file`.

## `/执行子阶段`

Goal: implement one sub-stage, then stop.

Rules:

- Read agent constitution and current stage implementation truth.
- If the task is lightweight, use `task-risk-gates.md` instead of forcing a stage truth document.
- If no current-stage implementation truth exists for standard/high-risk product code, stop and run `/功能开工评估` plus `/阶段计划`; do not code.
- If the current-stage implementation truth is not user-confirmed, stop and ask for confirmation.
- Only implement the named sub-stage.
- Do not move to the next sub-stage automatically.
- Do not change foundation documents, schema, stack, permissions, or directory architecture unless the sub-stage explicitly says so.
- If the requested work conflicts with truth docs, stop and run `/防漂移`.

Execution order:

```text
current truth
  -> owner and contract
  -> regression gate
  -> owner-layer implementation
  -> thin adapter/UI/CLI/API wiring
  -> targeted validation
  -> doc write-back
  -> git boundary check
```

Rules:

- Shared by two or more UI/API/CLI/provider/runtime paths means shared owner first, not duplicated adapter logic.
- UI, route handlers, controller, prompt text, local mock files, and temporary scripts must not own core business semantics.
- If the next sentence would be "we can extract it later", stop and put the concept in the right owner now.
- If the correct owner is unclear, stop and ask or do a read-only owner audit.
- Add or update the smallest gate that would catch the failure: unit test, contract test, fixture, API example, browser check, migration check, or manual user acceptance path.
- Do not add retries, sleeps, fallback branches, compatibility shims, or string contains checks unless evidence proves that mechanism is the real owner-layer fix.

Completion report:

- What was implemented.
- Files changed.
- What was intentionally not done.
- Validation run.
- Unverified items.
- Next sub-stage from the truth document.
