class Intake:
    def __init__(self):
        self.has_piece = False
        self.output = 0.0

    def update(self, request, enabled, detected):
        # TODO: implement the requirements from the project page.
        self.output = 0.0

    def stop(self):
        self.output = 0.0
