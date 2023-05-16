from itertools import permutations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230515 2503 숫자야구

# 정답코드

N = int(input())

numbers = []

for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3):
    temp = ''
    for c in perm:
        temp += str(c)
    numbers.append(int(temp))

def check(num: str, target: str, score: int) -> bool:
    
    res = 0

    target_list = list(target)
    for i in range(3):
        if num[i] in target_list:
            if num[i] == target[i]:
                res += 10
            else:
                res += 1
        
    if score == res:
        return True
    
    return False


for _ in range(N):
    target, strike, ball = map(int, input().split())

    for i in range(len(numbers)):
        
        if numbers[i] == 0:
            continue

        score = 10 * strike + ball

        if not check(str(numbers[i]), str(target), score):
            numbers[i] = 0

ans = 0
for n in numbers:
    if n > 0:
        ans += 1

print(ans)