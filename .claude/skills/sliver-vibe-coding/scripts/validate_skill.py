#!/usr/bin/env python3
"""Validate Sliver Vibe Coding skill structure without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "VERSION",
    "CHANGELOG.md",
    "COMPATIBILITY.md",
    "agents/openai.yaml",
    "references/task-risk-gates.md",
    "references/routes-intake.md",
    "references/routes-rescue.md",
    "references/routes-git.md",
    "references/routes-feature.md",
    "references/routes-backend.md",
    "references/routes-validation.md",
    "references/routes-release.md",
    "references/routes-constitution.md",
    "references/project-flow.md",
    "references/project-intake.md",
    "references/project-templates.md",
    "references/context-handoff.md",
    "references/question-bank.md",
    "references/tech-stack.md",
    "references/frontend-skeleton.md",
    "references/database-design.md",
    "references/backend-boundary.md",
    "references/backend-skeleton.md",
    "references/third-party-integration.md",
    "references/monetization-and-entitlements.md",
    "references/beginner-failure-modes.md",
    "references/security.md",
    "references/git-and-delivery.md",
    "references/agent-constitution.md",
    "references/agent-constitution-template.md",
    "scripts/evaluate_routes.py",
    "scripts/check_project_guardrails.py",
    "tests/route-eval-cases.json",
    "assets/project-bootstrap/AGENTS.md",
    "assets/project-bootstrap/dev-docs/README.md",
    "assets/project-bootstrap/dev-docs/project-brief.md",
    "assets/project-bootstrap/dev-docs/architecture.md",
    "assets/project-bootstrap/dev-docs/acceptance.md",
    "assets/project-adoption/AGENTS.md",
    "assets/project-adoption/dev-docs/README.md",
    "assets/project-adoption/dev-docs/current-state-audit.md",
    "assets/project-adoption/dev-docs/architecture.md",
    "assets/project-adoption/dev-docs/acceptance.md",
]

REQUIRED_ROUTES = [
    "/任务风险分级",
    "/立项",
    "/拆分",
    "/项目体检",
    "/环境启动",
    "/报错救援",
    "/AI债务体检",
    "/git保护",
    "/技术选型",
    "/第三方接入",
    "/收费权益设计",
    "/功能开工评估",
    "/阶段计划",
    "/执行子阶段",
    "/阶段验收",
    "/用户验收陪跑",
    "/质量验收",
    "/部署路线",
    "/发布准备",
    "/上下文交接",
    "/防漂移",
    "/生成宪法",
    "/宪法体检",
]

DOC_PATHS = [
    SKILL,
    ROOT / "README.md",
    *sorted((ROOT / "references").glob("*.md")),
]

FORBIDDEN_DOC_TERMS = [
    "原稿",
    "口播",
    "视频底稿",
    "实战篇",
    "source material",
    "source manuscript",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
    except UnicodeDecodeError as exc:
        fail(f"file is not valid UTF-8: {path.relative_to(ROOT)}: {exc}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md missing YAML frontmatter")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> None:
    if not ROOT.exists():
        fail(f"root does not exist: {ROOT}")

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"required file missing: {rel}")

    skill_text = read(SKILL)
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != "sliver-vibe-coding":
        fail("frontmatter name must be sliver-vibe-coding")
    description = frontmatter.get("description", "")
    if not description:
        fail("frontmatter description is empty")
    if not description.startswith("Use when "):
        fail("frontmatter description must start with 'Use when '")
    if len(description) > 1024:
        fail(f"description too long: {len(description)} characters")
    if "skill-fit assessment" not in description:
        fail("description must require lightweight skill-fit assessment for ordinary engineering tasks")

    if "references/commands.md" in skill_text:
        fail("SKILL.md should not route execution through monolithic references/commands.md")

    for route in REQUIRED_ROUTES:
        if route not in skill_text:
            fail(f"route missing from SKILL.md: {route}")

    referenced = set(re.findall(r"`(references/[^`]+?\.md)`", skill_text))
    for rel in referenced:
        if not (ROOT / rel).is_file():
            fail(f"SKILL.md references missing file: {rel}")

    commands_lines = len(read(ROOT / "references/commands.md").splitlines())
    if commands_lines > 120:
        fail(f"references/commands.md should stay an index, got {commands_lines} lines")

    all_docs = "\n".join(read(path) for path in DOC_PATHS if path.exists())
    for term in FORBIDDEN_DOC_TERMS:
        if term in all_docs:
            fail(f"forbidden source-provenance term found in skill docs: {term}")

    for required in [
        "普通工程任务",
        "轻量任务",
        "标准任务",
        "高风险任务",
        "Capability Platform Gate",
        "Frontend Design-System Gate",
        "Single Runtime",
        "Cross-Language Architecture Truth",
        "project-bootstrap",
        "project-adoption",
        "check_project_guardrails.py",
        "context-handoff",
        "HTTPS",
        "CHANGELOG.md",
        "COMPATIBILITY.md",
    ]:
        if required not in all_docs and required not in read(ROOT / "README.md"):
            fail(f"required governance/install term missing: {required}")

    cases_path = ROOT / "tests/route-eval-cases.json"
    try:
        import json

        case_count = len(json.loads(read(cases_path)))
    except Exception as exc:  # noqa: BLE001
        fail(f"route evaluation cases are invalid JSON: {exc}")
    if case_count < 40:
        fail(f"route evaluation should cover more than smoke tests, got {case_count} cases")

    print("OK: skill structure validated")


if __name__ == "__main__":
    main()
