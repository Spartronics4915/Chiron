"""Launch a canonical or student robot from the repository root."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("assignment", nargs="?", default="examples/mechanism/solution")
args = parser.parse_args()
robot = (ROOT / args.assignment / "robot.py").resolve()
if not robot.is_relative_to(ROOT) or not robot.is_file():
    parser.error("Choose a directory inside Chiron containing robot.py")
env = dict(os.environ, PYTHONPATH=os.pathsep.join([str(robot.parent), str(ROOT)]))
raise SystemExit(subprocess.call(
    [sys.executable, "-m", "robotpy", "--main", str(robot), "sim"], cwd=ROOT, env=env))
