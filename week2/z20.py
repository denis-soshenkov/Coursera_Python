a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1 > 0 and a2 > 0 and b1 > 0 and b2 > 0 and c1 > 0 and c2 > 0:
    if a1 > b1:
        (a1, b1) = (b1, a1)
    if a1 > c1:
        (a1, c1) = (c1, a1)
    if b1 > c1:
        (b1, c1) = (c1, b1)
    if a2 > b2:
        (a2, b2) = (b2, a2)
    if a2 > c2:
        (a2, c2) = (c2, a2)
    if b2 > c2:
        (b2, c2) = (c2, b2)
    a = (a1 // a2) * (b1 // b2) * (c1 // c2)
else:
    print(0)
