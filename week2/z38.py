N = int(input())
k = N
i = 0
while N != 0:
    N = int(input())
    if i == 0 and N < k:
        i = N
    elif N == k:
        i = N
    elif N > k:
        i = k
        k = N
print(i)
