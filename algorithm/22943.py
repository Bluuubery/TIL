import math
import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip("\r\n")

# 230320 22943 수

K, M = map(int, input().split())

MAX_NUM = 98765
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
prime = [0 for _ in range(MAX_NUM + 1)]

# 소수 구하기
for num in range(2, MAX_NUM + 1):

    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            break
    else:
        prime[num] = 1

# 숫자 구하기
numbers = []
for perm in permutations(NUMBERS, K):
    if perm[0] == 0:
        continue
    
    num = 0
    for i in range(K):
        num += perm[i] * 10**(K - i - 1)
    
    numbers.append(num)

# print(numbers)

set_1 = set()
set_2 = set()

# 조건 1
for num in numbers:
    for i in range(2, num // 2 + 1):
        target = num - i
        if target == i:
            continue
        if prime[target] and prime[i]:
            set_1.add(num)


# 조건 2
for num in numbers:

    target = num
    while True:
        if target < M:
            break
        if target % M:
            break
        target //= M

    for i in range(2, int(math.sqrt(target)) + 1):
        if target % i:
            continue
        if prime[i] and prime[target // i]:
            set_2.add(num)



print(len(set_1 & set_2))