import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230521 a 레몬 따기

# 정답코드

N = int(input())

lemons = list(map(int, input().split()))

print(max(list(lemons[i] - (N - i) for i in range(N))))
