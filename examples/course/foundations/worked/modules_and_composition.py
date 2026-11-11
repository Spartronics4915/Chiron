# This small standalone example demonstrates composition without needing another file.
class Intake:
    def __init__(self):
        self.output = 0.0

    def stop(self):
        self.output = 0.0

class Robot:
    def __init__(self):
        self.intake = Intake()

robot = Robot()
robot.intake.output = 0.4
robot.intake.stop()
print("Robot intake:", robot.intake.output)
