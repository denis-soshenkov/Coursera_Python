a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d:
    f = True
elif b <= d:
    f = True
elif c <= d:
    f = True
else:
    f = False
if a <= e:
    g = True
elif b <= e:
    g = True
elif c <= e:
    g = True
else:
    g = False
if f & g is True:
    print('YES')
else:
    print('NO')
