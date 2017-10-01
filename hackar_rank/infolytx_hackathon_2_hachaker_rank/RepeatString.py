#!/bin/python3


s = input().strip()
n = int(input().strip())

length = len(s);

ch = 'a';

count_of_ch = 0;
for i in s:
    if (i == ch):
        count_of_ch += 1;

res_count = count_of_ch * int((n / length));

if (n % length == 0):
    print(res_count);

else:
    remaining = n % length;
    remain_count = 0;

    for i in s[0:remaining]:
        if (i == ch):
            remain_count += 1;

    print(res_count + remain_count);
