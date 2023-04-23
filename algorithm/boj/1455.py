import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230414 1455 뒤집기2

# 정답코드

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

def flip(r, c):
    for i in range(r + 1):
        for j in range(c + 1):
            arr[i][j] = 0 if arr[i][j] else 1


ans = 0

for r in range(N - 1, -1, -1):
    for c in range(M - 1, -1, -1):
        if arr[r][c]:
            flip(r, c)
            ans += 1

print(ans)
