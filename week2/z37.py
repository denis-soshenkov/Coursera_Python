N = int(input())
k = N
i = 1
while N != 0:
    N = int(input())
    if k == N:
        i += 1
    elif N > k:
        k = N
        i = 1
print(i)
