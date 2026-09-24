class Intake:
    def __init__(self):
        self.has_piece = False
        self.output = 0.0

    def update(self, request, enabled, detected):
        self.has_piece = detected
        if not enabled:
            self.output = 0.0
        elif detected and request > 0:
            self.output = 0.0
        elif request > 1.0:
            self.output = 1.0
        elif request < -1.0:
            self.output = -1.0
        else:
            self.output = request

    def stop(self):
        self.output = 0.0
