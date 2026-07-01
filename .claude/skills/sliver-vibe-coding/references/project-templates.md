# Project Templates

Use this file when materializing project truth documents for a new project or a half-built project adoption.

The bundled templates are starting assets, not final truth. The agent must adapt them to the user's real project evidence before treating them as authoritative.

## Template Sets

### Empty Or New Project

Use `assets/project-bootstrap/` when the project has no real code, no business behavior, or only an empty directory.

Files:

- `assets/project-bootstrap/AGENTS.md`
- `assets/project-bootstrap/dev-docs/README.md`
- `assets/project-bootstrap/dev-docs/project-brief.md`
- `assets/project-bootstrap/dev-docs/architecture.md`
- `assets/project-bootstrap/dev-docs/acceptance.md`

Use this sequence:

```text
project root check
  -> Git/privacy baseline
  -> bootstrap AGENTS.md draft
  -> project brief
  -> technical selection
  -> architecture truth
  -> acceptance truth
  -> guardrail check
```

### Half-Built Or Inherited Project

Use `assets/project-adoption/` when the repo already has code, docs, deployment scripts, generated files, or AI-made behavior.

Files:

- `assets/project-adoption/AGENTS.md`
- `assets/project-adoption/dev-docs/README.md`
- `assets/project-adoption/dev-docs/current-state-audit.md`
- `assets/project-adoption/dev-docs/architecture.md`
- `assets/project-adoption/dev-docs/acceptance.md`

Use this sequence:

```text
read-only takeover audit
  -> dangerous adoption action check
  -> truth-root decision
  -> current-state audit
  -> architecture owner map
  -> acceptance truth
  -> guardrail check
  -> first safe task proposal
```

## Adaptation Rules

- Do not copy templates without project evidence.
- Replace generic sections with actual file paths, commands, owners, risks, and user decisions.
- If a section is unknown, write `未验证` and ask the smallest blocking question.
- Do not create `dev-docs/` if it is already occupied by non-development material; use `project-intake.md` to choose another truth root.
- Do not declare a truth root, rewrite AGENTS.md, move docs, or delete old docs without user confirmation in adoption mode.
- Keep public docs and internal truth docs separate.
- Before remote push, decide whether generated truth docs and AGENTS.md are public-safe or should stay private.

## Guardrail Check

After creating or changing the template-derived project truth, run:

```bash
python3 scripts/check_project_guardrails.py <project-root> --mode bootstrap
python3 scripts/check_project_guardrails.py <project-root> --mode adoption
```

When checking the bundled templates themselves, add `--allow-template`.

The guardrail script checks structure and obvious drift markers. It does not replace source reading, user confirmation, validation commands, or security review.
