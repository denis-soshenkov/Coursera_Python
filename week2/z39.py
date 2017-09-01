A = int(input())
Fn = 0
Fn1 = 0
Fn2 = 0
for i in range(A + 1):
    if i == 0:
        Fn2 == 0
        Fn == 0
    elif i == 1:
        Fn1 = 1
        Fn = 1
    else:
        Fn = Fn1 + Fn2
        Fn2 = Fn1
        Fn1 = Fn
print(Fn)
