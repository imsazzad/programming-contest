#!/bin/python3

def kangaroo(x1, v1, x2, v2):
    if (v2 == v1 and x2 == x1):
        return "YES";
    elif (v2 == v1):
        return "NO";
    if (x1 < x2 and v1 < v2):
        return "NO";
    elif (x2 < x1 and v2 < v1):
        return "NO";

    meeting_time = (x2 - x1) / (v1 - v2);
    meeting_time_int = int(meeting_time);
    if meeting_time - meeting_time_int > 0.0001:
        return "NO";
    else:
        return "YES";


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
