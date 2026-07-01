# Constitution Routes

Use this file with `agent-constitution.md` and `agent-constitution-template.md` when creating or auditing AGENTS.md or equivalent project agent rules.

## Contents

- `/生成宪法`
- `/宪法体检`

## `/生成宪法`

Goal: create a project-specific agent constitution from the bundled base template.

Required references:

- `agent-constitution.md`
- `agent-constitution-template.md`
- Project truth documents.
- Current code, package files, framework files, docs, scripts, tests, and Git state.

Procedure:

1. Run a read-only project evidence audit.
2. Produce an owner map for product, frontend, backend, database, auth, permissions, config, tests, docs, and Git.
3. Produce a template-clause mapping table. For each important base-template clause, mark it keep, rewrite, delete, or needs user decision.
4. Ask any blocking questions before drafting if evidence is missing or contradictory.
5. Draft the constitution using project-specific rules and evidence paths.
6. Run the anti-shallow validation in `agent-constitution.md`.
7. Only then write or update the actual agent instruction file if the user approved the path and direction.
8. After writing or changing the target file, run `scripts/check_project_guardrails.py <project-root> --mode constitution`.

Output before writing:

- Project evidence pack.
- Owner map.
- Clause mapping table.
- Missing evidence and user questions.
- Draft structure.
- Constitution guardrail plan.

Do not write the final constitution if the user has not approved the direction and the target file path.

## `/宪法体检`

Goal: determine whether an existing `AGENTS.md` or equivalent file is useful or only a shallow template adaptation.

Default mode is read-only. Inspect files and scripts, but do not run build, test, install, dev-server, codegen, deploy, migration, or preview commands unless the user explicitly approves, because those commands may write caches, generated files, build outputs, databases, or external state.

Check:

- Does it bind rules to actual files, owners, commands, and truth documents?
- Does it delete irrelevant template clauses?
- Does it distinguish universal rules from stack-specific adapters?
- Does it explain current product boundaries and rejected directions?
- Does it include real stop conditions?
- Does it include validation commands that exist in this repo?
- Does it avoid pretending missing backend/API/schema/docs already exist?
- Does it force document updates when truth changes?
- Would it pass the constitution guardrail without placeholders, empty critical fields, or generic rules?

Output:

- Project evidence pack.
- Owner map.
- Base-template clause mapping.
- Anti-shallow validation table.
- Verdict with threshold.
- Useful clauses.
- Shallow or generic clauses.
- Missing project-specific rules.
- Wrong or stale rules.
- Required questions.
- Rewrite plan.
