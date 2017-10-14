#!/bin/python3

dict = {}


def my_anagram(a, b):
    count = [0] * 26;
    for c in a:
        count[ord(c) - 97] += 1;
    for c in b:
        count[ord(c) - 97] += -1;
        if (count[ord(c) - 97] == -1):
            return 0;

    for c in count:
        if (c != 0):
            return 0;

    return 1;

def sherlockAndAnagrams(s):
    for i in range(len(s)):
        for j in range(0, len(s) - i):  # TODO not whole leght
            sub_string = s[i:i + j + 1]
            # print(sub_string);
            if (s != sub_string):
                try:
                    sub_array = dict[str(len(sub_string))];
                    sub_array.append(sub_string);
                    dict[str(len(sub_string))] = sub_array;

                except:
                    dict[str(len(sub_string))] = [sub_string];

    result = 0;
    for i in dict:
        # print(i, dict[i]);
        import itertools
        for a, b in itertools.combinations(dict[i], 2):
            result += my_anagram(a, b)
            # result += add_if_anagram(a, b)

    return result;


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    dict = {};
    result = sherlockAndAnagrams(s)
    print(result)

# def add_if_anagram(a, b):
#     if (sorted(a) == sorted(b)):
#         return 1;
#     else:
#         return 0;


# 5
# ifailuhkqq
# hucpoltgty
# ovarjsnrbf
# pvmupwjjjf
# iwwhrlkpek
