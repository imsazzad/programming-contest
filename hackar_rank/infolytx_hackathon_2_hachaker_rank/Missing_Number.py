# TODO this one causes runtime error TLE
# n_size = int(input().strip());
# n_ar = list(map(int, input().strip().split(' ')));
# n_ar.sort();
#
# m_size = int(input().strip());
# m_ar = list(map(int, input().strip().split(' ')));
# m_ar.sort();
#
#
# current = 0;
# result_arr = [];
# dict = {}
#
#
# for i in m_ar:
#     if(i != n_ar[current]):
#         try:
#             dict[str(i)] = 100;
#         except:
#             dict[str(i)] = 100;
#     else:
#         current += 1;
#
#
#
# for key, value in dict.items() :
#     result_arr.append(key);
#
# result_arr.sort();
#
# print(*result_arr);


# 10
# 203 204 205 206 207 208 203 204 205 206
# 13
# 203 204 204 205 206 207 205 208 203 206 205 206 204

n_size = int(input().strip());
n_ar = list(map(int, input().strip().split(' ')));

m_size = int(input().strip());
m_ar = list(map(int, input().strip().split(' ')));

count_array = [0] * 10000
result_array = [];

for i in n_ar:
    count_array[i - 1] += -1;

for i in m_ar:
    count_array[i - 1] += 1;

for index in range(len(count_array)):
    if count_array[index] > 0:
        result_array.append(index + 1);

print(*result_array);
