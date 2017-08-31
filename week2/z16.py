a = int(input())
b = int(input())
c = int(input())
if c < a:
    (c, a) = (a, c)
if b < a:
    (b, a) = (a, b)
if c < b:
    (c, b) = (b, c)
print(a, b, c)
