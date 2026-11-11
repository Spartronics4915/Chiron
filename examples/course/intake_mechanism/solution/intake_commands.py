import commands2
import wpilib


class Acquire(commands2.Command):
    def __init__(self, intake, timeout=2.0):
        super().__init__()
        self.intake = intake
        self.timeout = timeout
        self.timer = wpilib.Timer()
        self.succeeded = False
        self.addRequirements(intake)

    def initialize(self):
        self.timer.restart()
        self.succeeded = False

    def execute(self):
        self.intake.set_output(0.5)

    def isFinished(self):
        return self.intake.has_piece() or self.timer.hasElapsed(self.timeout)

    def end(self, interrupted):
        self.succeeded = not interrupted and self.intake.has_piece()
        self.intake.stop()
        self.timer.stop()


class Release(commands2.Command):
    def __init__(self, intake):
        super().__init__()
        self.intake = intake
        self.timer = wpilib.Timer()
        self.addRequirements(intake)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.intake.set_output(-0.5)

    def isFinished(self):
        return not self.intake.has_piece() or self.timer.hasElapsed(1.0)

    def end(self, interrupted):
        self.intake.stop()
        self.timer.stop()


class ManualIntake(commands2.Command):
    def __init__(self, intake, read_request):
        super().__init__()
        self.intake = intake
        self.read_request = read_request
        self.addRequirements(intake)

    def execute(self):
        self.intake.set_output(self.read_request())

    def end(self, interrupted):
        self.intake.stop()
