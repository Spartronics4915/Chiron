"""Periodic intake example; launch through tools/run_robot.py."""
import wpilib
from examples.support.intake_io import IntakeSim


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        if wpilib.RobotBase.isReal():
            raise RuntimeError("This course example is simulation-only")
        self.io = IntakeSim()
        self.timer = wpilib.Timer()
        wpilib.SmartDashboard.putNumber("Intake request", 0.0)
        wpilib.SmartDashboard.putBoolean("Piece available", True)

    def set_intake(self, request):
        if self.io.detected and request > 0:
            self.io.set_output(0.0)
        else:
            self.io.set_output(request)

    def teleopPeriodic(self):
        request = wpilib.SmartDashboard.getNumber("Intake request", 0.0)
        self.set_intake(request)

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        if self.timer.get() < 2.0:
            self.set_intake(0.5)
        else:
            self.set_intake(0.0)

    def disabledInit(self):
        self.io.set_output(0.0)

    def simulationPeriodic(self):
        self.io.enabled = self.isEnabled()
        self.io.piece_available = wpilib.SmartDashboard.getBoolean("Piece available", True)
        self.io.step()
        wpilib.SmartDashboard.putBoolean("Has piece", self.io.detected)
        wpilib.SmartDashboard.putNumber("Intake output", self.io.output)
