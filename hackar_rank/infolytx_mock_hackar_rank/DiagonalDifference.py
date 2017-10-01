#!/bin/python3


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diff = 0
col = 0
for row in range(n):
    diff += a[row][col] - a[row][n - col - 1]
    col += 1
if (diff < 0):
    diff *= -1
print(diff)
