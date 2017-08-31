A = int(input())
B = int(input())
C = int(input())
if A % 2 == 0:
    if B % 2 == 1:
        print('YES')
    elif C % 2 == 1:
        print('YES')
    else:
        print('NO')
elif A % 2 == 1:
    if B % 2 == 0:
        print('YES')
    elif C % 2 == 0:
        print('YES')
    else:
        print('NO')
elif B % 2 == 0:
    if A % 2 == 1:
        print('YES')
    elif C % 2 == 1:
        print('YES')
    else:
        print('NO')
elif B % 2 == 1:
    if A % 2 == 0:
        print('YES')
    elif C % 2 == 0:
        print('YES')
    else:
        print('NO')
elif C % 2 == 0:
    if B % 2 == 1:
        print('YES')
    elif A % 2 == 1:
        print('YES')
    else:
        print('NO')
elif C % 2 == 1:
    if B % 2 == 0:
        print('YES')
    elif A % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
