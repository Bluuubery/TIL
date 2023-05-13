# 1038 감소하는 수 230512

from itertools import combinations


N = int(input())

if N > 1022:
    print(-1)
    exit()

numbers = [str(i) for i in range(10)]
dec_nums = list()

for i in range(1, 11):
    for comb in combinations(numbers, i):
        dec_nums.append(int(''.join(sorted(comb, reverse=True))))

dec_nums.sort()

print(int(dec_nums[N]))

