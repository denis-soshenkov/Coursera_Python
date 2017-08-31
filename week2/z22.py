a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 or c == 0:
    print('NO')
elif -b % a != 0:
    print('NO')
elif c * (-b // a) + d == 0:
    print('NO')
elif b == 0:
    print('INF')
else:
    print(int(-b // a))
