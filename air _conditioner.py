troom, tcond = list(map(int, input().split()))
operating_mode = input()
if operating_mode == 'freeze':
    if troom > tcond:
        print(tcond)
    else:
        print(troom)
elif operating_mode == 'heat':
    if troom < tcond:
        print(tcond)
    else:
        print(troom)
elif operating_mode == 'auto':
    print(tcond)
elif operating_mode == 'fan':
    print(troom)
