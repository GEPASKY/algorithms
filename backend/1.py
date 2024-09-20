end = list()
for i in range(int(input())):
    data = input().split(",")
    fio = len(set("".join(data[:3])))
    sm_num = sum(map(int, "".join(data[3:5]))) * 64
    alf = "abcdefghijklmnopqrstuvwxyz"
    bgn_letter = (alf.index(data[0][0].lower()) + 1) * 256
    hex_result = hex(fio + sm_num + bgn_letter)[-3:].upper()
    encrypted_code = hex_result.zfill(3)
    end.append(encrypted_code)
print(*end)