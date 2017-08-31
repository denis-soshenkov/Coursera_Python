n = int(input())
if n > 10 and n < 21:
    print(n, 'korov')
elif n % 10 == 0 or n % 10 > 4:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
