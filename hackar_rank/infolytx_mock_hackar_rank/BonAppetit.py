#!/bin/python3

def bonAppetit(n, k, b, ar):
    summ = sum(ar);
    if (summ - ar[k]) / 2 == b:
        return 'Bon Appetit'
    else:
        return int(b - (summ - ar[k]) / 2)


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)

# 4 1
# 3 10 2 9
# 12
# ans = 5
#
# 4 1
# 3 10 2 9
# 7
# ans = 'Bon Appetit'
