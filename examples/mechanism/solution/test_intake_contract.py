"""A first subsystem check, also included directly in the beginner lesson."""
from intake_subsystem import Intake
from examples.support.intake_io import IntakeSim


def test_forward_request():
    io = IntakeSim()
    io.enabled = True
    intake = Intake(io)
    intake.set_output(0.5)
    assert io.output == 0.5
