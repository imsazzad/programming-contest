test_case = input().strip();
test_case = int(test_case);


def find_chile_optimized(a, b, depth, start_node):
    diff = b - a;

    lowest_node = start_node + depth * a;
    highest_node = start_node + depth * b;

    res_arr = [];
    if (diff == 0):
        res_arr.append(lowest_node);
        return res_arr;

    current_node = lowest_node;

    while (current_node <= highest_node):
        res_arr.append(current_node);
        current_node += diff;

    return res_arr;


for i in range(test_case):
    dict = {}
    num_of_stones = input().strip();
    num_of_stones = int(num_of_stones);

    a = input().strip();
    a = int(a);

    b = input().strip();
    b = int(b);

    if (b < a):
        a, b = b, a;

    final_res = find_chile_optimized(a, b, num_of_stones - 1, 0);
    print(*final_res);






#
# 2
# 3
# 1
# 2
# 4
# 10
# 100
# print(dict)


# 10
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
# 1000
# 1000
# 1
