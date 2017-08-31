x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) % 2 != 0:
    print('NO')
elif x1 < 1 or x1 > 8 or y1 < 1 or y1 > 8:
    print('NO')
elif x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8:
    print('NO')
elif y2 < y1 or x2 < x1:
    print('NO')
elif (x2 + y2) % 2 == 0 and x2 <= y2:
    print('YES')
else:
    print('NO')
