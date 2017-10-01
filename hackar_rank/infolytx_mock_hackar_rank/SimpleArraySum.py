#!/bin/python3


def simpleArraySum(n, ar):
    return sum(ar)


n = int(input().strip())
# TODO to make a stream to an array

inp = input().strip().split(' ')
print(inp);
ar = list(map(int, inp))
result = simpleArraySum(n, ar)
print(result)
