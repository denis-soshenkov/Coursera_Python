from math import ceil

H = int(input())
A = int(input())
B = int(input())

print(ceil((H - A) / (A - B)) + 1)
