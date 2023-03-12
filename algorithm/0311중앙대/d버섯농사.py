from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230311 중앙대 D 버섯농사

# 정답코드

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
max_mushroom = K * M

def bfs(r, c):
    global ans, K, max_mushroom
    
    queue = deque()
    queue.append((r, c))
    
    arr[r][c] = 1
    result = 1
    max_mushroom -= 1
    
    while queue:
        r, c = queue.popleft()


        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0 and max_mushroom > 0:
                    queue.append((nr, nc))
                    
                    arr[nr][nc] = 1
                    result += 1
                    max_mushroom -= 1

    if result % K:
        ans += (result // K) + 1
    else:
        ans += result // K

for r in range(N):
    for c in range(N):
        if arr[r][c] == 0:
            bfs(r, c)

if ans == 0:
    print("IMPOSSIBLE")
elif ans > M:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(M - ans)