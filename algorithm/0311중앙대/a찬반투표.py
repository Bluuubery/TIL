import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220311 중앙대 A 찬반투표

# 정답코드

N = int(input())

vote = list(map(int, input().split()))

cnt_a = 0
cnt_r = 0
cnt_i = 0

for v in vote:
    if v == -1:
        cnt_r += 1
    elif v == 0:
        cnt_i += 1
    else:
        cnt_a += 1

if N % 2 and cnt_i >= (N // 2) + 1:
    print("INVALID")
elif not N % 2 and cnt_i >= N // 2:
    print("INVALID")
elif cnt_r >= cnt_a:
    print("REJECTED")
else:
    print("APPROVED")

