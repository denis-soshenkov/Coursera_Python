N = int(input())
i = N
k = 0
while N != 0:
    N = int(input())
    if N > i:
        k += 1
    i = N
print(k)
