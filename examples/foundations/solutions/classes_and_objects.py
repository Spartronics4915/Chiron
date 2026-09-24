class Launcher:
    def __init__(self):
        self.target_speed = 0.0
        self.measured_speed = 0.0

left = Launcher()
right = Launcher()
left.target_speed = 1500.0
assert left.target_speed == 1500.0
assert right.target_speed == 0.0
print(left.target_speed, right.target_speed)
