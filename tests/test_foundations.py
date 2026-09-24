"""Execute maintained beginner programs; never run student submissions."""
from pathlib import Path
import subprocess
import sys
import pytest
from examples.intake_model.solution.intake import Intake

ROOT = Path(__file__).resolve().parents[1]
PROGRAMS = sorted((ROOT / "examples/foundations/worked").glob("*.py")) + sorted(
    (ROOT / "examples/foundations/solutions").glob("*.py")) + [
        ROOT / "examples/intake_model/solution/main.py"]


@pytest.mark.parametrize("program", PROGRAMS, ids=lambda p: str(p.relative_to(ROOT)))
def test_example_runs(program):
    subprocess.run([sys.executable, str(program)], check=True, capture_output=True, timeout=10)


@pytest.mark.parametrize("enabled", [False, True])
@pytest.mark.parametrize("detected", [False, True])
@pytest.mark.parametrize("motor_request", [-2, -1, -0.4, 0, 0.4, 1, 2])
def test_intake_model_contract(enabled, detected, motor_request):
    model = Intake()
    model.update(motor_request, enabled, detected)
    assert model.has_piece == detected
    if not enabled or (detected and motor_request > 0):
        assert model.output == 0
    else:
        assert -1 <= model.output <= 1
        assert model.output * motor_request >= 0
        assert abs(model.output) == min(abs(motor_request), 1)
    model.stop()
    assert model.output == 0 and model.has_piece == detected
