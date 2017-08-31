A = int(input())
if A % 4 == 0:
    if A % 400 == 0:
        if A % 100 != 0:
            print("YES")
        else:
            print("NO")
    print("NO")
print("NO")
