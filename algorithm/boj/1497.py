from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230405 1497 기타콘서트

# 정답코드

N, M = map(int, input().split())
guitar = set()


for i in range(N):
    name, can_play = input().split()

    binary_can_play = ''
    for j in range(M):
        if can_play[j] == 'Y':
            binary_can_play += '1'
        else:
            binary_can_play += '0'

    guitar.add(int(binary_can_play, 2))

ans = 0
max_cnt = 0

for i in range(1, N + 1):
    for comb in combinations(guitar, i):

        sum_play = 0
        for can_play in comb:
            sum_play |= can_play

        cnt = 0
        for j in range(M):
            if sum_play & (1 << j):
                cnt += 1
        
        if cnt > max_cnt:
            max_cnt = cnt
            ans = i

print(ans if ans else -1)

