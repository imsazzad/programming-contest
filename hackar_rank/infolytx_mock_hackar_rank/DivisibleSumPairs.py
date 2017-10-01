#!/bin/python3

def divisibleSumPairs(n, k, ar):
    total = 0
    for idx, val in enumerate(ar):
        j = idx + 1;
        while j < len(ar):
            if ((val + ar[j]) % k == 0):
                total += 1;
            j += 1;
    return total;


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)


# 6 3
# 1 3 2 6 1 2
# 5  Ans
