import math
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230311 연합 A 팝핀소다

# 정답코드

N, M, K = map(int, input().split())

ans = min(int(math.log2(K)) + M, int(math.log2(N)))

print(ans)