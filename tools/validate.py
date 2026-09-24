"""Run the same checks locally and in CI; leave a validated /Chiron artifact."""
from pathlib import Path
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "_build" / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)


def run(name, command, env=None):
    print(f"Checking {name}...", flush=True)
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True,
                            text=True, encoding="utf-8", errors="replace")
    output = result.stdout + result.stderr
    (REPORTS / f"{name}.log").write_text(output, encoding="utf-8")
    if result.returncode or "⛔" in output:
        print(output[-12000:])
        raise SystemExit(f"{name} failed; see _build/reports/{name}.log")
    print(f"Passed {name}", flush=True)


def clear_generated(name):
    target = (ROOT / "_build" / name).resolve()
    assert target.parent == (ROOT / "_build").resolve() and name in {"html", "site"}
    if target.exists():
        shutil.rmtree(target)


if __name__ == "__main__":
    python = sys.executable
    run("content", [python, "tools/check_content.py"])
    run("lint", [python, "-m", "ruff", "check", "examples", "tools", "tests"])
    run("examples", [python, "-m", "pytest", "-q", "--junitxml=_build/reports/tests.xml"])
    run("notebooks", [python, "tools/check_notebooks.py"])
    for version in ("basic", "solution"):
        run(f"robot-{version}", [python, "-m", "robotpy", "--main",
            f"examples/mechanism/{version}/robot.py", "test", "--builtin", "-j", "1", "--", "-q"])
    for label, base in (("root", ""), ("pages", "/Chiron")):
        clear_generated("html")
        clear_generated("site")
        env = dict(os.environ, BASE_URL=base)
        run(f"build-{label}", ["node", "node_modules/mystmd/dist/myst.cjs", "build",
                               "--html", "--strict", "--ci"], env)
        run(f"links-{label}", [python, "tools/check_links.py", "--base", base])
    print("Validation complete. Preview with: python tools/preview.py --base /Chiron")
