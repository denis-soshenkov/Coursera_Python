a = []
while True:
    a.append(int(input()))
    if len(a) > 5:
        break
print((a[3] * 3600 + a[4] * 60 + a[5]) - (a[0] * 3600 + a[1] * 60 + a[2]))
