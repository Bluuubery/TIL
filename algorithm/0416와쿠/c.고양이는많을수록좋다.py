import math
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230416 c 고양이는 많을수록 좋다

# 정답코드

N = int(input())

if N == 0:
    print(0)
    exit()

log_2 = int(math.log2(N))

if 2 ** log_2 == N:
    print(log_2 + 1)
else:
    print(log_2 + 2)

