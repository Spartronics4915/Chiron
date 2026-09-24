def clamp_request(request):
    if request > 1.0:
        return 1.0
    if request < -1.0:
        return -1.0
    return request

def intake_output(request, enabled, has_piece):
    if not enabled or (has_piece and request > 0):
        return 0.0
    return clamp_request(request)

assert intake_output(0.5, True, False) == 0.5
assert intake_output(0.5, True, True) == 0.0
assert intake_output(-0.5, True, True) == -0.5
assert intake_output(0.5, False, False) == 0.0
assert intake_output(2.0, True, False) == 1.0
assert intake_output(-2.0, True, True) == -1.0
print("Intake checks passed.")
