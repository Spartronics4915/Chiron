import commands2
from commands2.button import Trigger
import wpilib
from examples.support.intake_io import IntakeSim
from intake_subsystem import Intake
from intake_commands import Acquire, Release, ManualIntake


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        if wpilib.RobotBase.isReal():
            raise RuntimeError("This course example is simulation-only")
        self.io = IntakeSim()
        self.intake = Intake(self.io)
        self.acquire = Acquire(self.intake)
        self.release = Release(self.intake)
        self.intake.setDefaultCommand(ManualIntake(self.intake, self.read_request))
        for name in ("Acquire", "Release"):
            wpilib.SmartDashboard.putBoolean(name, False)
        wpilib.SmartDashboard.putBoolean("Piece available", True)
        wpilib.SmartDashboard.putNumber("Intake request", 0.0)
        self.acquire_trigger = Trigger(self.acquire_pressed)
        self.acquire_trigger.onTrue(self.acquire)
        self.release_trigger = Trigger(self.release_pressed)
        self.release_trigger.onTrue(self.release)

    def read_request(self):
        if self.isTeleopEnabled():
            return wpilib.SmartDashboard.getNumber("Intake request", 0.0)
        return 0.0

    def acquire_pressed(self):
        return self.isTeleopEnabled() and wpilib.SmartDashboard.getBoolean("Acquire", False)

    def release_pressed(self):
        return self.isTeleopEnabled() and wpilib.SmartDashboard.getBoolean("Release", False)

    def autonomousInit(self):
        self.acquire.schedule()

    def teleopInit(self):
        self.acquire.cancel()
        self.release.cancel()

    def disabledInit(self):
        commands2.CommandScheduler.getInstance().cancelAll()
        self.intake.stop()

    def simulationPeriodic(self):
        self.io.enabled = self.isEnabled()
        self.io.piece_available = wpilib.SmartDashboard.getBoolean("Piece available", True)
        self.io.step()
        wpilib.SmartDashboard.putBoolean("Has piece", self.intake.has_piece())
        wpilib.SmartDashboard.putNumber("Intake output", self.io.output)
        wpilib.SmartDashboard.putBoolean("Acquire succeeded", self.acquire.succeeded)
