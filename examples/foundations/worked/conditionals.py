enabled = True
has_piece = False
request = 0.6

# Choose an output; disabled behavior takes priority.
if not enabled:
    output = 0.0
elif has_piece:
    output = 0.0
else:
    output = request

print("Intake output:", output)
