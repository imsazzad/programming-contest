#!/bin/python3

dict = {}


def add_if_anagram(a, b):
    if (sorted(a) == sorted(b)):
        return 1;
    else:
        return 0;


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
            result += add_if_anagram(a, b)

    return result;


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    dict = {};
    result = sherlockAndAnagrams(s)
    print(result)
# 5
# ifailuhkqq
# hucpoltgty
# ovarjsnrbf
# pvmupwjjjf
# iwwhrlkpek
