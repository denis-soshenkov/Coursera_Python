a = int(input())
b = int(input())
c = int(input())
if a == c and a == b and b == c:
    print(3)
elif a == c:
    print(2)
elif b == c:
    print(2)
elif a == b:
    print(2)
else:
    print(0)
