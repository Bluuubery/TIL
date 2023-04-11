import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230405 17266 어두운 굴다리

# 정답코드

N = int(input())
M = int(input())
lamp = list(map(int, input().split()))



ans = max(N - lamp[-1], lamp[0] - 0)

for i in range(1, M):
    
    dist = lamp[i] - lamp[i - 1]
    height = dist // 2 + 1 if dist % 2 else dist // 2
    ans = max(ans, height)

print(ans)