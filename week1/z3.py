N = int(input())
N = N % 86400
h = N // 3600
mm = str((N % 3600) // 60)
ss = str((N % 3600) % 60)
if len(mm) == 1:
    mm = '0' + mm
if len(ss) == 1:
    ss = '0' + ss
print(h, mm, ss, sep=':')
