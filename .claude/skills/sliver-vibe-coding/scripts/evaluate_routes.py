#!/usr/bin/env python3
"""Run lightweight route regression checks for Sliver Vibe Coding."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CASES = ROOT / "tests/route-eval-cases.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")


def route_rows(skill_text: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in skill_text.splitlines():
        match = re.match(r"^\|\s*(`/.+?`)\s*\|.*\|\s*(.+?)\s*\|$", line)
        if not match:
            continue
        route = match.group(1).strip("`")
        rows[route] = match.group(2)
    return rows


def automatic_trigger_rows(skill_text: str) -> dict[str, list[str]]:
    try:
        section = skill_text.split("Common automatic triggers:", 1)[1].split("## Workflow Route Labels", 1)[0]
    except IndexError:
        fail("SKILL.md missing Common automatic triggers section")

    triggers: dict[str, list[str]] = {}
    for line in section.splitlines():
        if not line.strip().startswith("- "):
            continue
        phrases = re.findall(r'"([^"]+)"', line)
        routes = re.findall(r"`(/[^`]+)`", line)
        if "classify as" in line or "skill-fit assessment" in line:
            routes.append("/任务风险分级")
        if "current-stage implementation truth" in line:
            routes.append("/阶段计划")
        if not phrases or not routes:
            continue
        for phrase in phrases:
            triggers.setdefault(phrase, [])
            for route in routes:
                if route not in triggers[phrase]:
                    triggers[phrase].append(route)
    return triggers


def infer_routes(user_text: str, triggers: dict[str, list[str]]) -> list[str]:
    user_lower = user_text.lower()
    routes: list[str] = []
    for phrase, phrase_routes in triggers.items():
        if phrase.lower() not in user_lower:
            continue
        for route in phrase_routes:
            if route not in routes:
                routes.append(route)
    return routes


def main() -> None:
    skill_text = read(SKILL)
    rows = route_rows(skill_text)
    triggers = automatic_trigger_rows(skill_text)
    cases = json.loads(read(CASES))
    failures: list[str] = []
    covered_routes: set[str] = set()

    for case in cases:
        name = case["name"]
        user_text = case.get("user", "")
        route = case["expected_route"]
        if route not in rows:
            failures.append(f"{name}: expected route missing from route table: {route}")
            continue
        covered_routes.add(route)

        inferred_routes = infer_routes(user_text, triggers)
        if not inferred_routes:
            failures.append(f"{name}: user text did not match any automatic trigger: {user_text}")
        elif route not in inferred_routes:
            failures.append(
                f"{name}: expected {route}, got inferred routes {inferred_routes} for user text: {user_text}"
            )

        row = rows[route]
        for rel in case.get("expected_files", []):
            if rel not in row:
                failures.append(f"{name}: expected file not routed: {rel}")
            if not (ROOT / rel).is_file():
                failures.append(f"{name}: expected file missing on disk: {rel}")

        for phrase in case.get("trigger_terms", []):
            if phrase.lower() not in user_text.lower():
                failures.append(f"{name}: trigger phrase missing from user text: {phrase}")
            if phrase not in triggers:
                failures.append(f"{name}: trigger phrase missing from automatic trigger map: {phrase}")

        for phrase in case.get("required_reference_terms", []):
            found = any(phrase in read(ROOT / rel) for rel in case.get("expected_files", []) if (ROOT / rel).is_file())
            if not found:
                failures.append(f"{name}: required reference term not found: {phrase}")

        expected_class = case.get("expected_class")
        if expected_class:
            if expected_class not in skill_text and expected_class not in read(ROOT / "references/task-risk-gates.md"):
                failures.append(f"{name}: expected class not documented: {expected_class}")

    uncovered_routes = [route for route in rows if route not in covered_routes]
    if uncovered_routes:
        failures.append(f"route table has no evaluation case for: {', '.join(uncovered_routes)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        sys.exit(1)

    print(f"OK: {len(cases)} route evaluation cases passed")


if __name__ == "__main__":
    main()
