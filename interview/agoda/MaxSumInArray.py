def get_max_sum_in_array(array):
    index_minus_1_sum = 0
    index_minus_2_sum = 0
    current_sum = 0
    for index, current_value in enumerate(array):
        print("index_minus_2_sum :", index_minus_2_sum)
        print("index_minus_1_sum :", index_minus_1_sum)
        print("current_sum :", current_sum)
        print("current_value :", current_value)
        print("index :", index)
        print("--------------------------------------")
        # print(index_minus_2_sum, index_minus_1_sum, current_sum, current_value, index)
        if index == 0:
            current_sum = current_value
            continue
        elif index == 1:
            index_minus_1_sum = current_sum
            current_sum = max(current_sum, current_value)
            continue
        # elif index == 2:
        #     index_minus_2_sum = index_minus_1_sum
        #     index_minus_1_sum = current_sum
        #     current_sum = max(array[1], current_value + array[0])
        #     continue
        else:
            index_minus_2_sum = index_minus_1_sum
            index_minus_1_sum = current_sum
            current_sum = max(index_minus_1_sum, current_value + index_minus_2_sum)
            continue

    return current_sum


if __name__ == '__main__':
    assert (get_max_sum_in_array([100])) == 100
    assert (get_max_sum_in_array([100, 10])) == 100
    assert (get_max_sum_in_array([100, 101])) == 101
    assert (get_max_sum_in_array([100, 105, 1])) == 105
    assert (get_max_sum_in_array([100, 102, 5])) == 105
    assert (get_max_sum_in_array([100, 102, 5, 8])) == 110
    assert (get_max_sum_in_array([100, 102, 11, 8])) == 111
    assert (get_max_sum_in_array([110, 102, 11, 15])) == 125
