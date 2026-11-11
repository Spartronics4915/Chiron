enabled = True
has_piece = True
request = -0.4
if not enabled:
    output = 0.0
elif has_piece and request > 0:
    output = 0.0
else:
    output = request
print("Intake output:", output)
