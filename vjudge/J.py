from sys import stdin

dictionary = {}


def cycle_for_single_number(number):
    try:
        if (dictionary[str(number)]):
            return int(dictionary[str(number)]);
    except:
        if (number == 1):
            dictionary[str(number)] = 1;
            return 1;
        else:
            cycle = 0;

            if (number % 2 == 0):
                cycle = 1 + cycle_for_single_number(number // 2);
            elif (number % 2 == 1):
                cycle = 1 + cycle_for_single_number(3 * number + 1);

                dictionary[str(number)] = cycle;

            return cycle;


def get_max_cycle_number(a, b):
    max_cycle = 0
    for i in range(a, b + 1):
        temp = cycle_for_single_number(i);
        if (temp > max_cycle):
            max_cycle = temp;

    return max_cycle;


for line in stdin:
    if (line.strip()):
        array = list(line.strip().split(' '));
        if (len(array) == 2):
            a = int(array[0]);
            b = int(array[1]);
            if (a > b):
                print(a, b, get_max_cycle_number(b, a));
            else:
                print(a, b, get_max_cycle_number(a, b));

# 1 10
# 100 200
# 201 210
# 900 1000
# 1 1000000
