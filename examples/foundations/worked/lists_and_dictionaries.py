readings = [False, False, True]
detected_count = 0
for detected in readings:
    if detected:
        detected_count = detected_count + 1
print("Samples:", len(readings))
print("Detected samples:", detected_count)

inputs = {"request": 0.5, "enabled": True}
print("Requested output:", inputs["request"])
