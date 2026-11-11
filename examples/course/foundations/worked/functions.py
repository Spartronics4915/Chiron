def choose_output(request, enabled):
    if not enabled:
        return 0.0
    return request

result = choose_output(0.4, True)
print("Enabled:", result)
print("Disabled:", choose_output(0.4, False))
