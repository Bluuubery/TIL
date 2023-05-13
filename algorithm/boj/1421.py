import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230508 1451 나무꾼 이다솜

# 정답코드

N, C, W = map(int, input().split())

trees = []

for _ in range(N):
    trees.append(int(input()))

max_tree = max(trees)

answer = 0

# 1 ~ 가장 긴 나무의 길이까지 자르기
for i in range(1, max_tree + 1):

    temp = 0

    for tree in trees:

        sale = (tree // i) * W * i
        # 딱 맞게 잘릴 경우에는 1 빼기
        cost = C * (tree // i if tree % i else tree // i - 1)
        profit = sale - cost

        # 이익이 0보다 클 경우에만 더해주기
        if profit > 0:
            temp += profit

    answer = max(answer, temp)

print(answer)
