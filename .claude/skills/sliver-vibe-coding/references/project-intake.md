# Existing Project Intake

Use `/接管项目` for any non-empty project, half-built project, inherited repo, rescue request, or unclear current state.

## Read-Only First Pass

Inspect without editing:

- Repo boundary and nested repos.
- Git status and recent commits when useful.
- Directory tree.
- Package/framework files.
- Run/test scripts.
- Runtime version files, lockfiles, env examples, startup proof, and known startup blockers.
- Existing docs, especially `dev-docs`, `docs`, `AGENTS.md`, `README`, architecture docs, schema/migrations.
- Existing agent-instruction files such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, and whether they are generic or project-bound.
- Frontend, backend, database, and deployment structure.
- Duplicate/generated/AI-sprawl clues: repeated components, repeated APIs, dead files, mock data, custom wrappers, abandoned backups, and inconsistent patterns.
- Config examples and secret risks.
- `.gitignore`, tracked/private-file risks, nested Git repos, and third-party reference projects placed inside the project tree.

Do not start by generating a new architecture.

## Current Truth Summary

Return:

- Project type and likely product form.
- Existing stack.
- Stack, framework, SDK, and dependency fit: viable, questionable, or mismatch.
- Existing truth documents.
- Existing agent constitution quality.
- Existing frontend/backend/database status.
- Runtime/startup baseline status.
- AI-generated debt status.
- Git safety status.
- `.gitignore` and private-file status.
- Quality evidence status.
- Release/deployment/operations readiness when relevant.
- Missing or stale truth documents.
- Immediate risks.
- Best entry command.

## Stage Mapping

Map the project to one of these:

- Needs project brief backfill.
- Needs function list and stage plan.
- Needs technical route review.
- Needs runtime/startup baseline.
- Needs AI debt cleanup before more feature work.
- Needs frontend skeleton consolidation.
- Needs database design repair.
- Needs backend boundary definition.
- Needs backend skeleton validation.
- Needs security validation.
- Ready for current stage implementation truth.
- Ready for one sub-stage execution.
- Needs quality validation.
- Needs release readiness check.
- Needs deployment-route decision.
- Needs stack/framework/SDK route decision.

## Development Docs Audit

Use `/整理开发资料` when:

- `dev-docs/` does not exist.
- `dev-docs/` exists but contains non-development material.
- Development material is scattered across `docs/`, `README`, root markdown files, chat exports, issue notes, or random folders.
- Multiple docs disagree about product scope, stack, architecture, schema, or current stage.

Default to read-only audit first. Do not create, move, rename, delete, archive, or rewrite docs until the user approves the target structure.

## If `dev-docs/` Is Missing

1. Search for existing internal development docs in `docs/`, root markdown files, `.agents`, `.codex`, `README`, architecture docs, design docs, schema/migrations, and planning files.
2. If no internal-doc convention exists, propose `dev-docs/` as the internal truth root.
3. Ask for confirmation before creating it.
4. If the user confirms, choose the correct template set from `references/project-templates.md`: bootstrap templates for empty projects, adoption templates for half-built or inherited projects.
5. Create only the minimal truth index and the current required truth files. Do not create a pile of empty documents.
6. Run `scripts/check_project_guardrails.py <project-root> --mode bootstrap` or `--mode adoption` after creating or changing the truth surface.
7. Explain that internal truth docs are private by default and should not be pushed to a public remote unless the user explicitly approves.

Minimal first files:

- `dev-docs/README.md` or `dev-docs/truth-index.md`.
- Current project evidence summary.
- Links to existing source docs instead of duplicating them.

## If `dev-docs/` Exists But Is Not Development Material

Do not hijack it.

1. Identify what it actually contains.
2. Treat it as occupied by another purpose.
3. Propose a separate internal truth root, such as `internal-dev-docs/` or `docs/internal/`, matching repo style.
4. Ask the user to choose before creating anything.
5. Record in the truth index why `dev-docs/` was not used.

## If Development Docs Are Messy

Produce a docs inventory table:

| File | Current role | Status | Action |
| --- | --- | --- | --- |
| path | project brief / architecture / schema / stale / public docs / unknown | active / stale / conflict / duplicate / unrelated | keep / link / merge / archive / ask |

Then produce a target truth map:

- Product brief owner.
- Function list owner.
- Stage plan owner.
- Technical selection owner.
- Frontend architecture owner.
- Database design owner.
- Backend architecture owner.
- Security boundary owner.
- Monetization/entitlement owner.
- Agent constitution owner.
- Current stage implementation truth owner.
- Runtime/startup owner.
- Quality evidence owner.
- User acceptance owner.
- AI debt owner.
- Deployment route owner.
- Release/operations owner.

Rules:

- Do not move files during the audit.
- Do not delete stale docs until the user confirms.
- Prefer creating an index that marks active, stale, conflict, duplicate, public, or unrelated before reorganizing files.
- Public docs and internal truth docs must stay separate.
- If two docs conflict, report evidence and ask which truth wins.
- If the user wants version history for internal truth docs, suggest a separate local-only Git repo for that docs root instead of mixing it with public code delivery by default.

## `/整理开发资料`

Goal: turn scattered or missing development docs into a clear truth-document structure.

Output before edits:

- Current docs inventory.
- Conflicts and stale docs.
- Recommended truth root.
- Proposed file map.
- Files to keep as public docs.
- Files to archive or mark stale.
- Questions requiring user decision.

After approval:

- Create or update the truth index.
- Link to existing docs where possible.
- Move or archive only paths the user approved.
- Update `AGENTS.md` or equivalent only if the user approves the new truth root.
- If templates are used, adapt them to actual project evidence before treating them as truth.
- Run the project guardrail script and report failures as `未验证` or blockers.

## Existing Project Guardrails

- Do not say the workflow cannot apply because the project did not start from zero.
- Do not delete or rebuild working code to match the ideal sequence.
- Do not switch framework, stack, SDK, provider library, or integration style just because it is not the agent's preferred default.
- If the current route is materially worse for maintainability, security, deployment, official support, or product fit, run `/技术选型` and ask the user to choose before changing it.
- Do not add compatibility layers unless the user approves after seeing the tradeoff.
- If current code violates architecture, identify the owner layer and repair there.
- If documentation is stale, update the truth document before implementation.

## Adoption Template And Guardrail

For half-built projects with no reliable internal truth, use the adoption template set:

```text
assets/project-adoption/
  AGENTS.md
  dev-docs/README.md
  dev-docs/current-state-audit.md
  dev-docs/architecture.md
  dev-docs/acceptance.md
```

Do not write these files automatically just because they exist in the skill. First report the dangerous adoption action and ask the user to confirm the truth-root and AGENTS.md target.

After the user confirms and the files are adapted, run:

```bash
python3 scripts/check_project_guardrails.py <project-root> --mode adoption
```

If the repo uses a different internal docs directory, pass `--truth-dir <dir>` and record that decision in the truth index.
