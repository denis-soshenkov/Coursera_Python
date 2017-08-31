Ac = int(input())
Ar = int(input())
Bc = int(input())
Br = int(input())
if Ac == Bc or Ac - Bc == 1 or Bc - Ac == 1:
    if Ar == Br or Ar - Br == 1 or Br - Ar == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
