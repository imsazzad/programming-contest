#!/bin/python3

h = list(map(int, input().strip().split(' ')))
word = input().strip()
max_h = 0

for i in word:
    index = ord(i) - 97
    if (h[index] > max_h):
        max_h = h[index];

print(max_h * len(word))

# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
# ans = 9
#
# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
# zaba
#
# ans = 28
