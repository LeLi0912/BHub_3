# Compatibility

## Supported Runtime

- Codex skill folder format with a root `SKILL.md`.
- Optional metadata file: `agents/openai.yaml`.
- Optional bundled references under `references/`.
- No runtime dependency is required to use the skill.

## Validation Runtime

The validation scripts require:

- Python 3.9 or newer.
- Standard library only. No PyYAML or package installation is required.

Run:

```bash
python3 scripts/validate_skill.py
python3 scripts/evaluate_routes.py
```

## Installation Methods

HTTPS works for users without a configured Gitee SSH key:

```bash
git clone https://gitee.com/sliver-ring_admin/sliver-vibe-coding.git ~/.codex/skills/sliver-vibe-coding
```

SSH works when the user already has Gitee SSH access:

```bash
git clone git@gitee.com:sliver-ring_admin/sliver-vibe-coding.git ~/.codex/skills/sliver-vibe-coding
```

## Fixed Version

For a fixed install, pin the exact commit after cloning:

```bash
cd ~/.codex/skills/sliver-vibe-coding
git rev-parse HEAD
git checkout <commit-hash-from-previous-command>
```

If a release tag has been published, the tag can be used instead:

```bash
git checkout v0.1.0
```

## Upgrade

```bash
cd ~/.codex/skills/sliver-vibe-coding
git pull --ff-only
python3 scripts/validate_skill.py
python3 scripts/evaluate_routes.py
```

Review `CHANGELOG.md` before upgrading in a shared workflow.
