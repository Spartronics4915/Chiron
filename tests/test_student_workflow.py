"""Verify copied assignments refuse overwrite and survive an upstream lesson fix."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def tmp_path():
    # Keep disposable repositories inside the known workspace on restricted hosts.
    scratch = (ROOT / "_build" / "workflow-tests").resolve()
    assert scratch.is_relative_to(ROOT / "_build")
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="case-", dir=scratch) as directory:
        yield Path(directory)


def test_copy_refuses_overwrite(tmp_path):
    (tmp_path / "tools").mkdir()
    starter = tmp_path / "examples/foundations/starter"
    starter.mkdir(parents=True)
    (starter / "main.py").write_text('print("original")\n')
    shutil.copy2(ROOT / "tools/start_exercise.py", tmp_path / "tools/start_exercise.py")
    command = [sys.executable, str(tmp_path / "tools/start_exercise.py"), "foundations"]
    subprocess.run(command, check=True, capture_output=True)
    assignment = tmp_path / "student-work/foundations/main.py"
    assignment.write_text('print("my work")\n')
    retry = subprocess.run(command, capture_output=True)
    assert retry.returncode != 0
    assert assignment.read_text() == 'print("my work")\n'
    subprocess.run(command + ["--name", "fresh-attempt"], check=True, capture_output=True)
    assert (tmp_path / "student-work/fresh-attempt/main.py").read_text() == 'print("original")\n'


def test_upstream_lesson_fix_preserves_assignment(tmp_path):
    def git(*args):
        return subprocess.run(["git", "-C", str(tmp_path), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    git("init", "-b", "main")
    git("config", "user.name", "Course workflow test")
    git("config", "user.email", "course-test@example.invalid")
    (tmp_path / "lesson.md").write_text("Original lesson\n")
    git("add", ".")
    git("commit", "-m", "baseline")
    git("switch", "-c", "learning")
    student = tmp_path / "student-work/intake.py"
    student.parent.mkdir()
    student.write_text("# A student's saved assignment\n")
    git("add", ".")
    git("commit", "-m", "student work")
    git("switch", "main")
    (tmp_path / "lesson.md").write_text("Compatible lesson correction\n")
    git("add", ".")
    git("commit", "-m", "upstream fix")
    fix = git("rev-parse", "HEAD")
    git("switch", "learning")
    git("branch", "backup-before-update")
    git("merge", "--no-edit", fix)
    assert student.read_text() == "# A student's saved assignment\n"
    assert (tmp_path / "lesson.md").read_text() == "Compatible lesson correction\n"
