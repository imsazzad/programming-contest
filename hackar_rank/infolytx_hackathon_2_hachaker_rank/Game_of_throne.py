#!/bin/python3

arr = [0] * 26;


def gameOfThrones(s):
    for i in s:
        index = ord(i) - 97;
        arr[index] += 1;

    odd_count = 0;

    for i in arr:
        if (odd_count > 1):
            print("NO");
            return;
        if (i % 2 == 1):
            odd_count += 1;

    print("YES");


s = input().strip()
gameOfThrones(s)
