num0 = list(map(int, filter(lambda x: x in '1234567890', input())))
number0 = num0[-7:-1]
code0 = num0[-10:-7]
for i in range(3):
    s = input()
    num = list(map(int, filter(lambda x: x in '1234567890', s)))
    number = num[-7:-1]
    code = num[-10:-7]
    if (s.startswith('7') and len(code) != 0) or (len(s) in [11, 7]):
        print('NO')
        break
    if len(code) == 0:
        code = [4, 9, 5]
    if number0 == number and code0 == code:
        print('YES')
    else:
        print('NO')
