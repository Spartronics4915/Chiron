class Intake:
    def __init__(self):
        self.has_piece = False
        self.output = 0.0

front = Intake()
rear = Intake()
front.has_piece = True
print("Front:", front.has_piece)
print("Rear:", rear.has_piece)
