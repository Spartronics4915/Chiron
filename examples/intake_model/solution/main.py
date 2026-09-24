from intake import Intake


class Robot:
    def __init__(self):
        self.intake = Intake()


robot = Robot()
robot.intake.update(0.5, True, False)
assert robot.intake.output == 0.5
robot.intake.update(0.5, True, True)
assert robot.intake.output == 0.0
robot.intake.update(-0.5, True, True)
assert robot.intake.output == -0.5
robot.intake.update(-0.5, False, True)
assert robot.intake.output == 0.0
robot.intake.update(2.0, True, False)
assert robot.intake.output == 1.0
robot.intake.update(-2.0, True, True)
assert robot.intake.output == -1.0
other_robot = Robot()
assert not other_robot.intake.has_piece
robot.intake.stop()
assert robot.intake.output == 0.0
print("Model checks passed.")
