"""Copy a fresh exercise into your committable student-work directory."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
STARTERS = {"foundations": "examples/foundations/starter",
            "intake-model": "examples/intake_model/starter",
            "periodic-intake": "examples/mechanism/basic",
            "intake-subsystem": "examples/mechanism/basic"}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("exercise", choices=STARTERS)
parser.add_argument("--name", help="Optional fresh destination name")
args = parser.parse_args()
name = args.name or args.exercise
if not name or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for c in name):
    parser.error("Name must contain lowercase letters, digits, - or _")
dest = ROOT / "student-work" / name
if dest.exists():
    parser.error(f"{dest} already exists; choose --name for a fresh copy")
shutil.copytree(ROOT / STARTERS[args.exercise], dest,
                ignore=shutil.ignore_patterns("__pycache__"))
print(f"Created {dest.relative_to(ROOT)}. Your original examples are unchanged.")
