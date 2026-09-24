class Intake:
    def __init__(self):
        self.has_piece = False
        self.output = 0.0

    def update(self, request, enabled, detected):
        self.has_piece = detected
        if not enabled or (detected and request > 0):
            self.output = 0.0
        else:
            self.output = request

    def stop(self):
        self.output = 0.0

intake = Intake()
intake.update(0.5, True, False)
print("Acquiring:", intake.output)
intake.update(0.5, True, True)
print("Detected:", intake.output)
intake.update(-0.5, True, True)
print("Releasing:", intake.output)
intake.stop()
print("Stopped:", intake.output)
