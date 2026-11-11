from intake import Intake

intake = Intake()
intake.update(0.5, True, False)
print("Requested collection, got:", intake.output)
# Add a Robot class, a sequence of inputs, and assertions as described in the lesson.
