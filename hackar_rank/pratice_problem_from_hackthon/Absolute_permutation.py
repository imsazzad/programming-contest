#!/bin/python3

def get_permutation(n, k):
    if (k == 0):
        return list(range(1, n + 1));

    batch_size = 2 * k;
    if (n % batch_size != 0):
        return -1;

    resultant_array = [0] * (n + 1);  # not using array index 0

    for i in range(int(n / batch_size)):
        for j in range(1, int(batch_size / 2) + 1):
            batch_start_point = (i * batch_size);
            swap_element_1 = batch_start_point + j;
            swap_element_2 = batch_start_point + j + k;

            resultant_array[swap_element_2] = swap_element_1;
            resultant_array[swap_element_1] = swap_element_2;

    return resultant_array[1:];


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    result = get_permutation(n, k);
    if (result == -1):
        print("-1");
    else:
        print(*result);



# k = 1 = n - 1 => 2 er product
# k = 2 = n - 2 => 4 er product
# k = 3 = n - 3 => 6 er product
# 1 2 3 4 5 6 7 8

# 3
# 2 1
# 3 0
# 3 2

# 1
# 2 1
