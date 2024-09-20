all_logs = dict()

# let's write the values ​​in a dictionary for convenience
cnt = int(input())
for i in range(cnt):
    log = input().split()
    if log[3] not in all_logs:
        all_logs[log[3]] = [[log[0], log[1], log[2], log[4]]]
    else:
        all_logs[log[3]].append([log[0], log[1], log[2], log[4]])

print(all_logs)

# sort values in dict for convenience
for key, value in all_logs.items():
    values = sorted(value, key=lambda x: (int(x[0]), int(x[1]), int(x[2]), x[3]))
    all_logs[key] = values

print(all_logs)

scripts = ["ABS", "ABC", "AC"]

for key, value in all_logs.items():
    sm = 0
    script = ""
    for i in range(len(value)):
        event = value[i]
        script += event[-1]
        if script in scripts:
            sm_01 = int(event[0]) * 24 * 60 +int(event[1]) * 60 + int(event[2])
            sm += sm_01 - sm_00
            script = ""
        if script == "A":
            sm_00 = int(event[0]) * 24 * 60 + int(event[1]) * 60 + int(event[2])
    print(str(sm), end=' ')
    
        
