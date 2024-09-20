all_logs = dict()

# Read log entries
cnt = int(input())
for i in range(cnt):
    log = input().split()
    rocket_id = log[3]
    if rocket_id not in all_logs:
        all_logs[rocket_id] = [[log[0], log[1], log[2], log[4]]]
    else:
        all_logs[rocket_id].append([log[0], log[1], log[2], log[4]])

# Sort log entries
for key, value in all_logs.items():
    sorted_values = sorted(value, key=lambda x: (int(x[0]), int(x[1]), int(x[2]), x[3]))
    all_logs[key] = sorted_values

# Define scripts
scripts = ["ABS", "ABC", "AC"]

# Calculate total movement time for each rocket
for key, value in all_logs.items():
    total_time = 0
    script = ""
    start_time = 0
    for event in value:
        script += event[-1]
        if script in scripts:
            end_time = int(event[0]) * 24 * 60 + int(event[1]) * 60 + int(event[2])
            total_time += end_time - start_time
            script = ""
        if script == "A":
            start_time = int(event[0]) * 24 * 60 + int(event[1]) * 60 + int(event[2])
    print(total_time, end=' ')
