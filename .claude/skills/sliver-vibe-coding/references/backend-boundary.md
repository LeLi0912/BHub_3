# Backend Boundary

Use `/后端边界` before backend implementation or when the user is unsure whether a backend is needed.

## Script Or Project Backend

First distinguish:

- Small script: file processing, spreadsheet cleanup, image compression, single API call, scheduled local task, one-off automation.
- Project backend: users, orders, content publishing, permissions, payments, reviews, analytics, API service, multi-user data.

Do not force a full backend onto a small script.

## Project Backend Responsibilities

A project backend usually handles:

- Business rules.
- Data flow.
- API collaboration with frontend.
- Authentication.
- Authorization.
- Ownership checks.
- Validation.
- External service calls.
- Tasks or jobs.

Explain that frontend is for user operation, database is for storage, and backend decides whether an action can happen and how data changes.

Business rules that affect money, permissions, ownership, status, inventory, quotas, or database writes must not live only in the frontend. Hiding a button is not the same as backend enforcement.

## Before Code

Ask or derive:

- Which business rules must be enforced by backend.
- Which APIs frontend needs.
- Which tables each API reads or writes.
- Which APIs require login.
- Which APIs require roles.
- Which operations must be limited to owner data.
- Error response rules.
- Authentication approach.
- Permission entry point.

Ask business questions before code questions. Do not start by asking the user to choose a language or framework when the backend's responsibility is still unclear.

If backend is needed, route next to `/后端架构` before `/后端骨架`. The boundary decision says what backend owns; the architecture truth says how backend work is organized.

## Language And Framework

Recommend one backend language and framework based on project facts.

General tendencies:

- Python: automation, data, AI apps, lightweight backend.
- Node.js/TypeScript: full-stack web teams, JavaScript/TypeScript frontend alignment.
- Go: deployable API services, concurrency, cloud-style backend.
- Java: enterprise systems, complex backend, organization standards.
- PHP: mature web projects when ecosystem or deployment fit.

Framework matters more than language for project quality because it defines routing, project structure, validation, logging, configuration, database access, and error handling.

For non-technical users, prefer a framework with clear conventions and documentation.

If the backend language, framework, or core SDK changes later, write the reason, impact, and migration plan into the truth document before coding. Do not let the project drift between languages or frameworks through casual feature work.

## Single Runtime Default

For MVP and non-technical users, prefer one main backend runtime/language when it can cover the product's API, automation, data, AI, and job needs with acceptable official SDK support and framework structure.

Do not split backend work across languages simply because different examples or libraries are familiar. A second runtime creates extra owners: API contract, process startup, ports, env files, auth propagation, logs, tracing, tests, deployment, rollback, and debugging.

Recommend cross-language only when a required SDK/platform/native capability, existing stable service, isolation need, or company constraint proves the split is necessary. If cross-language is recommended, require the `Cross-Language Architecture Truth` from `tech-stack.md` before coding.

## Output

Write:

- Whether backend is needed.
- Backend responsibilities.
- API boundary.
- Required auth and permission model.
- Data read/write responsibility.
- Recommended language and framework.
- Single-runtime or cross-language decision and reason.
- Framework built-in capabilities.
- Extra SDKs or libraries needed.
- Required backend architecture truth sections that must be created before skeleton code.
- What must be written into truth docs.
