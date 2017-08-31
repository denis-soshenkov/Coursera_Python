A = input()
if len(A) < 4:
    A = '0' * (4 - len(A)) + A
B = [char for char in A]
if B[0] == B[3] and B[1] == B[2]:
    print(1)
else:
    print(0)
