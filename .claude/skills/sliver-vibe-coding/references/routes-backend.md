# Backend Routes

Use this file with `backend-boundary.md`, `backend-skeleton.md`, and `security.md` for backend architecture and skeleton validation routes.

## Contents

- `/后端架构`
- `/骨架验收`

## `/后端架构`

Goal: create or audit backend architecture truth before backend skeleton or business backend code.

Procedure:

1. Read project brief, function list, complex-feature docs, stage plan, technical selection, database design, and security notes.
2. Confirm backend scope: what backend owns, what frontend owns, what database owns, and what is out of scope.
3. Confirm one backend language/framework route and why common alternatives are not primary.
4. Define request lifecycle: route/controller, validation, auth, permission/ownership, service/business rule, data access/transaction, response/error/log.
5. Define owner layer map for routes/controllers, services, models/entities, repositories/DAO/ORM, middleware/guards, validators, config, errors, logs, jobs, tests, and docs.
6. Define API contract rules: route pattern, request shape, response shape, HTTP status, pagination/list, error code/message, and versioning if needed.
7. Define data, transaction, migration/schema, auth, permission, config, secret, logging, and external provider boundaries.
8. Define the new-module placement rule.
9. Define validation commands and evidence required before business development.
10. Ask blocking questions if any owner boundary is unclear.

Output:

- Backend scope.
- Recommended backend architecture route.
- Request lifecycle.
- Owner layer map.
- API contract rules.
- Data/auth/permission/config/logging boundaries.
- Framework-first rules and forbidden custom wrappers.
- New-module placement rule.
- Validation evidence required.
- `未验证` items and user decisions.

Backend architecture is invalid if it only lists directories, skips business boundary, cannot name owner layers, ignores framework conventions, lacks request lifecycle, or cannot say how a new module should be added.

## `/骨架验收`

Use the backend skeleton validation procedure in `backend-skeleton.md`. Do not accept a claim that the skeleton is usable without runtime evidence.
