from decimal import *
from sys import stdin

for line in stdin:
    if (line.strip()):
        ar = list(line.strip().split(' '));
        if (len(ar) == 1):
            n = int(ar[0]);
            result = n * n + 1;
            result = result // 2;
            result = Decimal(result) * Decimal(result);
            print(int(result));
            # 1562437500625000000
            # 1562562500625000000
