k = int(input())
if k > 0:
    if k % 3 == 0:
        print('YES')
    elif k % 5 == 0:
        print('YES')
    elif k % 8 == 0:
        print('YES')
    elif k - 5 > 0 and (k - 5) % 3 == 0:
        print('YES')
    elif k - 3 > 0 and (k - 3) % 5 == 0:
        print('YES')
    elif k - 10 > 0 and (k - 10) % 3 == 0:
        print('YES')
    elif k - 6 > 0 and (k - 6) % 5 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
