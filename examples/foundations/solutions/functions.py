def intake_output(request, enabled, has_piece):
    if not enabled:
        return 0.0
    if has_piece and request > 0:
        return 0.0
    return request

print(intake_output(0.5, True, False))
print(intake_output(0.5, True, True))
print(intake_output(-0.5, True, True))
print(intake_output(-0.5, False, True))
