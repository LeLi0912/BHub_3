# Release Routes

Use this file for deployment-route decisions, release readiness, and drift control.

## Contents

- `/部署路线`
- `/发布准备`
- `/上下文交接`
- `/防漂移`

## `/部署路线`

Goal: choose one deployment route before the agent changes external state or treats a preview URL as production.

Use this when the user asks where to deploy, wants a public URL, plans to hand off to a client/team, or has a stack but no production route.

Procedure:

1. Confirm the release target: local self-use, internal team, private beta, client delivery, public production, or demo only.
2. Read current stack, framework docs, package scripts, backend/database/storage/auth/provider needs, and deployment files.
3. Classify the app form: static frontend, SPA, full-stack web, API backend, serverless function, worker, mobile app, mini program, desktop/local tool, or automation script.
4. Compare deployment options and choose one primary route. Prefer managed, mainstream, official or framework-recommended routes for non-technical users when they fit.
5. Check environment separation, env vars, secret storage, production owner, and placeholder docs.
6. Check database, storage, migration, backup, restore, rollback, and seed data needs.
7. Check public/private exposure: app privacy setting, admin path, upload files, internal docs, generated assets, preview URLs, and search-engine indexing risk.
8. Check domain, HTTPS, CORS, OAuth redirect URI, webhook URL, callback verification, and provider console settings.
9. Check monitoring/logs, health check, support owner, cost/quota/billing owner, and provider lock-in.
10. Ask the user to approve the route before `/发布准备`.

Output:

- Recommended deployment route.
- Why it fits this project.
- Rejected routes and why.
- Required accounts and services.
- Env/secret plan.
- Data/migration/backup/rollback plan.
- Public/private exposure decision.
- Cost/quota notes.
- Pre-release blockers.
- User approval needed.

Invalid:

- Saying "just deploy to Vercel/Netlify/Render" without stack and backend/data evidence.
- Skipping privacy settings for public URLs.
- Treating preview deployment as production readiness.

## `/发布准备`

Goal: prepare a project or stage to be used outside local development by real users, a team, or a customer.

Do not deploy first and explain later. Produce a release readiness report before changing external state.

Check:

- Release target: local handoff, internal team, private beta, public production, or client delivery.
- Environment separation: local, test/staging, production.
- Build/run commands and exact artifacts.
- Environment variables, secret storage, `.env.example`, key rotation needs, and production secret ownership.
- Domain, callback URLs, OAuth redirect URIs, webhook URLs, CORS, HTTPS, storage bucket, email/SMS/payment/provider console settings when relevant.
- Database migration plan, seed data, backup, restore, rollback, and data-loss risk.
- Third-party production/sandbox switch, quota, billing, rate limits, webhook signature, idempotency, and failure handling.
- Security/privacy: sensitive data, logs, admin accounts, password reset, access control, legal/license concerns when relevant.
- Monitoring and support: health check, error logs, request logs, alert owner, support path, known unverified items.
- Cost and resource limits: hosting, database, storage, provider API, email/SMS/payment fees, expected first-month risk.
- Public surface: README or handoff notes, user instructions, admin instructions, not internal truth docs.
- Fake-done check: no mock data, fake success state, unconnected backend, skipped migration, or sample-provider path is being presented as real production behavior.
- Git/release checkpoint: branch, commit, tag or release note when appropriate.

Output:

- Release readiness verdict: `可发布`, `可内测`, `暂缓发布`, or `禁止发布`.
- Blocking issues.
- Pre-release checklist.
- Deployment steps.
- Rollback steps.
- Post-release verification.
- Known risks and owners.
- User confirmations required.

Release is invalid if rollback, secrets, database migration, third-party production settings, or monitoring/log evidence are skipped while the project is meant for real users.

If release is not completed in the current window, or another agent/user will continue the release, run `/上下文交接` before ending.

## `/上下文交接`

Goal: produce a copy-paste-ready continuation packet for a new window, another agent, or a handoff after a partially completed stage.

Use `context-handoff.md`.

Procedure:

1. Inspect current git state for the main repo and any nested internal-doc repo.
2. Capture latest commits, changed files, untracked files, and staged files.
3. Name the active truth documents and current project/stage boundary.
4. Summarize completed work by owner layer, not by vague time order.
5. Record validation commands and exact pass/fail status.
6. Record runtime state: URLs, servers, ports, deploy state, device/provider state, and stale process warnings if relevant.
7. List blocked evidence and unresolved user decisions.
8. Add drift warnings: what the next agent must not change, restart, delete, or assume.
9. Give exact next safe commands or the next recommended route.

Output:

- Markdown handoff block.
- Git state.
- Current truth.
- Completed work.
- Changed files.
- Validation evidence.
- Runtime state.
- Drift warnings.
- Next safe steps.

Invalid:

- Omitting dirty/untracked files.
- Saying tests passed without commands.
- Omitting nested repo state.
- Giving a generic "continue from here" prompt without paths, files, commands, and boundaries.

## `/防漂移`

Goal: recover alignment before code gets worse.

Procedure:

1. Quote or summarize the conflicting request, plan, or implementation.
2. Compare it with the relevant truth document.
3. Decide whether the change affects foundation.
4. If it affects foundation, stop and ask the user to choose a redesign path.
5. If it is a normal requirement change, update the truth document first, then continue.

Output:

- Drift point.
- Affected truth document.
- Foundation impact.
- Recommended action.
- User decision needed.
- Whether a handoff is needed to preserve the corrected boundary.
