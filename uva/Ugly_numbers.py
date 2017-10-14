# 5^0   * 3^0  * 2^0
# 5^0   * 3^0  * 2^1
# 5^0   * 3^1  * 2^0
# 5^1   * 3^0  * 2^0
# 5^0   * 3^1  * 2^1
# 5^0   * 3^0  * 2^3
#
#
#
#
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
#

ugly_numbers = []
ugly_numbers.append(1);

current_2 = 0;
current_3 = 0;
current_5 = 0;

while (len(ugly_numbers) < 1500):
    new_2 = ugly_numbers[current_2] * 2;
    new_3 = ugly_numbers[current_3] * 3;
    new_5 = ugly_numbers[current_5] * 5;

    new_ugly = min(new_2, new_3, new_5);
    if (ugly_numbers[-1] != new_ugly):
        ugly_numbers.append(new_ugly);

    if (new_ugly == new_2):
        current_2 += 1;
    elif (new_ugly == new_3):
        current_3 += 1;
    elif (new_ugly == new_5):
        current_5 += 1;

print("The 1500'th ugly number is", str(ugly_numbers[1499]) + ".")
print("The 1500'th ugly number is <number>.")
