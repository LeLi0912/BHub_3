# Technical Selection

Use `/技术选型` to choose or review a project stack.

## Principles

- Product form comes before technology stack.
- Platform capability comes before web/desktop/backend choices.
- Give one primary recommendation, not a menu of equal options.
- Alternatives are evidence, not choices. The user should see one recommended route plus rejected routes and reasons.
- Prefer mature, documented, community-active, AI-familiar technology.
- Prefer convention-heavy frameworks and official SDKs that give strong project structure, routing, validation, config, error handling, component patterns, testing, and deployment conventions.
- Prefer stacks that reduce from-scratch work: use established framework scaffolds, UI libraries, admin templates, ORM/migration tools, auth libraries, provider SDKs, and framework-supported patterns when they fit the project.
- Prefer routes that non-technical users can run and deploy with managed services, clear docs, predictable env vars, and simple rollback when that fits the product.
- Avoid asking non-technical users to maintain hand-rolled component systems, custom framework skeletons, custom SDK wrappers, or low-level glue code unless the project has a clear reason.
- Avoid asking non-technical users to maintain loosely governed style utilities, scattered component snippets, dual runtimes, or cross-language glue unless the project has a clear reason and truth documents to control it.
- Avoid technology chosen for prestige, novelty, performance theater, or vague safety feelings.
- Prefer one main runtime/language for MVP delivery when one stack can cover the product. Cross-language architecture is an exception that must be justified.
- Once selected, the route should not move without a written reason and truth-doc update.
- Real project needs override generic preference. If the most AI-familiar or most structured option conflicts with the user's product form, platform, deployment, budget, legal/license needs, team constraints, or existing system, choose the project-fit route and explain the tradeoff.

## Required Inputs

- Product form: website, mini program, app, admin system, script, backend API, or mixed product.
- MVP scope.
- Target users.
- Deployment expectation.
- Required platform capabilities: browser web, desktop app, local system automation, browser extension, CLI/background worker, mobile app, or hybrid.
- Login, roles, payments, uploads, or sensitive data.
- Team constraints, company constraints, historical systems, or required platforms.

## Source Materials Gate

Before recommending a stack, audit every available project-intake source. Do not finalize technical selection from only the latest chat message when project materials exist.

Read or explicitly mark missing:

- Project brief or立项文档.
- User roles, usage scenarios, MVP scope, and non-goals.
- Function list.
- Complex-feature documents.
- Large stage plan.
- Current-stage implementation truth if the stack decision is for an existing stage.
- Existing architecture, frontend, backend, database, security, deployment, or agent-constitution docs.
- Existing code evidence: package files, lockfiles, framework files, route/module layout, database/schema/migration files, scripts, and deployment files.
- Runtime evidence: install/start/build commands, env examples, local service requirements, and whether the project can currently run.
- User constraints: company rules, platform requirements, budget, launch speed, public/private deployment, commercial-use/license requirements, and maintenance capability.
- Third-party provider/API/SDK requirements.
- Local OS, desktop software, browser-control, file-system, keyboard/mouse, screen-capture, background-process, or system-automation requirements.
- User-provided references, screenshots, examples, or competitor products.

If documents are missing, stale, or contradictory, output a source coverage report and ask only the blocking questions before finalizing. If a reasonable temporary recommendation is still useful, label it `暂定技术路线`, list `未验证` items, and do not write it as final truth.

## Capability Platform Gate

Before recommending a stack, classify the product's required capabilities by platform.

Required capability classes:

- Browser-only web: pages, forms, dashboards, content, user flows, API calls, uploads within browser limits.
- Desktop app: local windows, native menus, tray, filesystem access, local credentials, local devices, long-running local process.
- Local system automation: operating local software, keyboard/mouse, screen capture, OS permissions, background automation, local files, or local device control.
- Browser extension: browser tab context, content scripts, browser permissions, website automation inside a browser.
- CLI/background worker: scheduled jobs, file processing, data sync, local or server-side automation without a full GUI.
- Hybrid: any combination of web UI plus local agent, desktop shell, extension, or background service.

Rules:

- Do not finalize a browser-only web stack when the requested capability requires local OS, desktop software, keyboard/mouse, screen capture, local files beyond browser limits, or persistent local background execution.
- If the capability class is unclear, ask blocking questions before producing a final stack.
- If a hybrid route is needed, define which process owns the UI, which process owns local capability, how they communicate, and what validation proves the bridge works.
- A web UI can be part of the solution, but it must not pretend to own capabilities that only a desktop, extension, local agent, CLI, or backend worker can safely provide.

Output a platform-fit table:

- Required capability.
- Platform class.
- What browser/web can own.
- What requires desktop/local/extension/worker/backend.
- Primary route.
- Rejected route and why.
- Unverified capability questions.

Technical selection is invalid if it recommends a web-only route for local system or desktop capability without either asking blocking questions or designing the required bridge.

## Frontend Design-System Gate

Frontend stack selection must distinguish a design system from implementation tools.

Rules:

- A low-constraint styling utility, raw CSS approach, ad hoc component snippet set, or copy-pasted component collection is not a complete design system by itself.
- A frontend route is valid only when it names the design token owner, theme/style entry point, component owner, reuse rule, and validation method for UI consistency.
- For non-technical users, prefer a structured UI/component route that reduces visual improvisation and gives clear component states, layout rules, accessibility basics, and token usage.
- If a low-level or utility-first styling route is recommended, it must be framed as an implementation layer under a token and component governance rule, not as the design truth.

The recommendation must include:

- Design-system owner: file path or intended truth doc.
- Token strategy: where colors, spacing, typography, radius, layout, and states are defined.
- Component strategy: chosen UI/component base, business-component layer, reuse rule, and forbidden mixed systems.
- Style drift prevention: what is not allowed, such as page-local visual systems, arbitrary one-off values, or multiple competing component styles.
- Validation: screenshot, token usage check, component reuse evidence, or UI review path.

Technical selection is invalid if it recommends a weakly governed styling/tooling route without design tokens, component ownership, and style-drift prevention.

## Single Runtime And Cross-Language Gate

Default to one main backend runtime/language for the MVP when one stack can cover the product's backend, automation, AI, data, and API needs.

Cross-language is allowed only when current evidence proves at least one of these:

- A required official SDK, platform API, model/runtime, native capability, or provider contract is only practical in another language.
- The project already has a stable service in another language and replacing it is riskier than integrating it.
- A specific workload needs process isolation, deployment isolation, performance characteristics, or dependency isolation that cannot be handled safely in the main runtime.
- Team/company constraints require a second runtime.

Do not recommend two backend runtimes simply because both are familiar, fashionable, or convenient for different examples. If one language/framework can cover the product with acceptable structure and official SDK support, choose the single-runtime route and list the rejected split route.

If cross-language remains the recommendation, create a `Cross-Language Architecture Truth` section before coding. It must define:

- Service/process ownership and repo layout.
- API contract or messaging contract, including versioning and compatibility.
- Shared schema/DTO strategy and source of truth.
- Local startup order, ports, health checks, and developer command map.
- Environment variables, secrets, config ownership, and example files.
- Auth/session/permission propagation across processes.
- Error model, status codes, retry/idempotency, timeout, and failure handling.
- Logging, trace/correlation ID, metrics, and debugging path across runtimes.
- Data consistency, transaction boundary, jobs/queues, and rollback strategy.
- CI/test matrix, contract tests, deployment topology, release order, and rollback plan.

Technical selection is invalid if it recommends cross-language architecture without proving why a single-runtime route is insufficient and without the cross-language truth above.

## Framework And SDK Preference Gate

When choosing a framework, SDK, UI library, database tool, auth provider, payment provider, map provider, AI provider, storage provider, messaging provider, analytics tool, or admin/dashboard base, score candidates against these priorities:

1. Project fit: matches the user's product form, MVP, roles, data, security, deployment, and business constraints.
2. AI familiarity: common enough that coding agents are likely to know the ecosystem, file layout, and common errors.
3. Strong conventions: gives clear directories, lifecycle, routing, validation, data access, error handling, testing, and deployment rules.
4. Less from-scratch work: provides reliable scaffolding, templates, UI components, SDK methods, auth/payment/provider flows, or migration tools.
5. Official or mature source: official SDK/framework/provider tooling first; mature community packages only when official tooling is absent or unsuitable.
6. Documentation and examples: current docs, quickstarts, examples, API references, and troubleshooting material.
7. Maintenance and safety: recent releases, active issues, security advisories, license/commercial-use fit, and migration path.
8. Operational simplicity: simple local startup, managed deployment fit, clear env/secrets model, logging/monitoring path, backup/rollback feasibility, and predictable cost.

The recommended route should normally choose the candidate that best satisfies these priorities together, not the one that is most fashionable or most flexible.

Do not choose a lower-level library, bare runtime, raw HTTP integration, blank CSS/component setup, or custom skeleton when a mature convention-based framework or official SDK fits the same business result.

If a from-scratch or low-level route is still recommended, the output must explain:

- Which real project need requires it.
- Which mature/official route was rejected.
- What extra owner rules, tests, docs, and maintenance burden this creates.
- What the non-technical user must understand before approving it.

## No Intake Material Gate

If there is no reliable project-intake material, do not make a final technical selection.

First ask the user to complete the minimum pre-stack facts:

- Product form or likely product form.
- Target user.
- First complete user flow.
- MVP scope.
- Explicit non-goals.
- Core business objects or data.
- Login, roles, payments, uploads, sensitive data, third-party integrations, or deployment constraints.
- Launch target: local use, internal team, public users, client delivery, or production.

Then route to `/立项` or `/拆分` as needed:

- Use `/立项` when product, user, MVP, or non-goals are unclear.
- Use `/拆分` when the idea exists but function list, complex features, or large stages are missing.
- Return to `/技术选型` only after the minimum facts are confirmed or written into a truth document.

A temporary recommendation is allowed only when the user explicitly needs direction now. Label it `暂定技术路线`, name the missing facts, and do not write it as the final technical-selection truth.

## Output Format

Write:

- Project evidence reviewed: file paths, user answers, existing code evidence, and missing or conflicting inputs.
- Recommended product form.
- Required capability and platform-fit table.
- Recommended frontend stack if needed.
- Frontend design-system and token strategy if frontend exists.
- Recommended backend language/framework if needed.
- Runtime/language boundary: single-runtime route or justified cross-language route.
- Recommended database.
- UI library or component approach if needed.
- Main SDKs or services.
- Framework/SDK preference score: project fit, AI familiarity, convention strength, from-scratch reduction, official/mature source, docs, maintenance/security/license.
- Runtime/deployment fit: how the route will start locally and where it can be deployed without forcing the user into unnecessary infrastructure work.
- Cross-language architecture truth when more than one runtime/language is recommended.
- Why this route fits.
- Why common alternatives are not the primary route.
- Risks and future re-evaluation triggers.
- What must be written into project truth documents.

The output must contain exactly one primary recommended route. It may compare alternatives, but it must not present multiple equal choices unless the user explicitly asks for a tradeoff discussion instead of a decision.

Technical selection is invalid if:

- It cannot name the project evidence reviewed.
- There is no reliable project-intake material and it does not route the user to `/立项` or `/拆分` first.
- It ignores available project brief, function list, stage plan, architecture, existing code, or user constraints.
- It skips capability-platform classification when the project mentions desktop, local system, browser automation, files, devices, background jobs, or software operation.
- It gives multiple equal recommendations instead of one primary route.
- It treats a low-constraint styling utility, raw CSS route, or ad hoc component snippets as a complete frontend design system.
- It recommends more than one backend runtime/language without proving why one runtime cannot cover the MVP.
- It recommends cross-language architecture without `Cross-Language Architecture Truth`.
- It recommends a weakly structured, low-level, from-scratch, custom-wrapper, raw-API, or hand-rolled component route without proving why mature convention-based frameworks, UI libraries, official SDKs, or framework-supported patterns do not fit.
- It recommends a third-party provider, SDK, or API route without `/第三方接入` evidence when that route is material to the project.
- It does not write the selected route back to the technical-selection truth document or clearly state that the route is only `暂定`.

## Reliability Checks

When recommending open source libraries or SDKs, check:

- Whether it is official or framework-recommended.
- Whether coding agents are likely to understand the common patterns.
- Whether it provides strong conventions instead of forcing custom glue.
- Whether it reduces from-scratch implementation.
- Maintenance status.
- Documentation quality.
- Issue activity.
- Recent releases.
- License and commercial-use restrictions.
- Security advisories when relevant.

If current information can change, verify with current primary sources before making a final recommendation.

For third-party providers, APIs, SDKs, OAuth flows, payments, maps, AI services, storage, messaging, analytics, or platform services, run `/第三方接入` before locking the route. Do not recommend an integration path from memory alone.

## Existing Project Review

For existing projects, do not restart selection casually.

Review:

- Whether current stack matches product form and scope.
- Whether the stack is unnecessarily heavy.
- Whether the stack is too obscure for AI-assisted maintenance.
- Whether framework norms are documented.
- Whether new dependencies violate the current route.
- Whether the current SDK is official, maintained, documented, and compatible with the provider's current API.
- Whether the current integration uses raw HTTP or a custom wrapper where an official SDK would reduce risk.
- Whether a non-official SDK or obsolete framework creates security, maintenance, deployment, or hiring/AI-maintenance risk.

Only recommend migration when current stack creates a real maintainability, security, deployment, or product-fit problem.

## Existing Stack Mismatch Gate

If the inherited project uses a framework, SDK, library, or stack that is not the current best route, do not silently switch it and do not shame the existing choice. Produce a decision note first.

Classify the current route:

- `继续沿用`: viable for the current product; document conventions and continue.
- `沿用但修正`: keep stack, repair owner boundaries, docs, scripts, or dependency versions.
- `局部替换`: replace a risky SDK/library/provider adapter without changing the whole stack.
- `分阶段迁移`: current route blocks maintainability, security, deployment, or product fit; migration needs its own implementation truth.
- `立即停止`: current route has a critical security, data-loss, license, platform, or provider-contract risk.

Before asking the user to switch, show:

- Current evidence: package files, framework files, SDK imports, lockfile versions, docs, API calls, or runtime constraints.
- Why the current route is acceptable or risky for this project.
- The recommended route.
- The cost of switching now.
- The cost of staying now.
- What can be safely repaired without switching.
- What data, auth, API, schema, or deployment areas migration would touch.
- A user-facing question: keep and repair, locally replace SDK/library, or approve migration planning.

If the user chooses migration, write or update the technical selection truth and a dedicated implementation truth before coding. Do not mix migration with a normal feature sub-stage.

## Feature Access Route Review

Before adding a feature, do not reopen the whole stack unless `/功能开工评估` proves the current foundation cannot support the business result.

Choose the access route in this order:

1. Reuse the existing owner module and pattern.
2. Extend an existing page, component, service, API, or schema area.
3. Add a sibling module that follows current framework conventions.
4. Add a provider adapter only after `/第三方接入` proves the official contract.
5. Propose foundation redesign only when the current route creates a real maintainability, security, deployment, or business-fit problem.

The recommendation must explain why the chosen route is better than the rejected routes for this project, not just why it is technically possible.
