N = int(input())
if N == 0:
    print('NO')
if N > 0:
    for i in range(N):
        if 2 ** i == N:
            print('YES')
            break
    if i + 1     w== N:
        print('NO')
