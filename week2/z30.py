import math as m
N = int(input())
if m.log2(N) % 1 == 0:
    print('YES')
else:
    print('NO')
