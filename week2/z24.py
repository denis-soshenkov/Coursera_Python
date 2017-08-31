N = int(input())
i = 1
if N != 0:
    while (i ** 2) <= N:
        print(i ** 2, end=' ')
        i = i + 1
else:
    print(0)
