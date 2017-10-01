n = input().strip()
n = int(n)

ar = list(map(int, input().strip().split(' ')))
ar.sort(reverse=True);

miles = 0
for i in range(len(ar)):
    miles += ar[i] * (2 ** i);

print(miles);

# 3
# 1 3 2
