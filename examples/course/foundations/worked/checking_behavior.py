def clamp_request(request):
    if request > 1.0:
        return 1.0
    if request < -1.0:
        return -1.0
    return request

assert clamp_request(0.4) == 0.4
assert clamp_request(2.0) == 1.0
assert clamp_request(-2.0) == -1.0
assert clamp_request(1.0) == 1.0
print("All request checks passed.")
