#!/bin/python3


def getTotalX(a, b):
    total_factor = 0;
    a.sort();
    b.sort();
    i = a[-1]
    while i <= b[0]:
        flag = True;
        for j in a:
            if (i % j != 0):
                flag = False;
                break;
        for k in b:
            if (k % i != 0):
                flag = False;
                break;
        if flag == True:
            total_factor += 1
        i += a[-1]
    return total_factor;


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)



    # 2 3
    # 4 2
    # 32 16 96
    # ans 3
