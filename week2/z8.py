a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1 < 1 or a2 < 1 or b1 < 1 or b2 < 1:
    print('NO')
if a1 > 8 or a2 > 8 or b1 > 8 or b2 > 8:
    print('NO')
if (a1 + a2) % 2 == (b1 + b2) % 2:
    print('YES')
else:
    print('NO')
