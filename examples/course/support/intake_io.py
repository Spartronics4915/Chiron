"""Supplied simulation: request [-1, 1], seconds, idealized piece detection.

Students program decisions, not this model. No physical device is controlled.
"""


class IntakeSim:
    def __init__(self):
        self.enabled = False
        self.piece_available = True
        self.detected = False
        self.output = 0.0
        self.elapsed = 0.0

    def set_output(self, request):
        self.output = max(-1.0, min(1.0, request)) if self.enabled else 0.0

    def step(self, dt=0.02):
        if not 0 < dt <= 0.1:
            raise ValueError("Step must be in (0, 0.1] seconds")
        if not self.enabled:
            self.output = 0.0
        collecting = self.output > 0 and not self.detected and self.piece_available
        releasing = self.output < 0 and self.detected
        if collecting or releasing:
            self.elapsed += dt
            if self.elapsed >= 0.4:
                self.detected = collecting
                self.elapsed = 0.0
        else:
            self.elapsed = 0.0
