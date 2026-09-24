requests = [0.2, 0.8, 0.4, 0.9]
high_requests = []
for request in requests:
    if request > 0.5:
        high_requests.append(request)
report = {"limit": 0.5, "high_requests": high_requests}
print(requests, len(requests))
print(high_requests, len(high_requests))
print(report)
