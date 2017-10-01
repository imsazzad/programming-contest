# !/bin/python3


def leftRotation(a, r):
    from collections import deque
    d = deque(a);
    d.rotate(-r);
    return d;


if __name__ == "__main__":
    import collections;

    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d);
    result = list(collections.deque(result));
    print(" ".join(map(str, result)))
