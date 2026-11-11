import commands2


class Intake(commands2.Subsystem):
    def __init__(self, io):
        super().__init__()
        self.io = io

    def set_output(self, request):
        if self.has_piece() and request > 0:
            self.io.set_output(0.0)
        else:
            self.io.set_output(request)

    def has_piece(self):
        return self.io.detected

    def stop(self):
        self.io.set_output(0.0)
