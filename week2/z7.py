x = int(input())
y = int(input())
if y % (y + 1 - x) == 0:
    print('YES')
else:
    print('NO')
