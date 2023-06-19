from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230615 111123 양 한마리... 양 두마리...

# 정답코드

N = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, R, C):

    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1

    while queue:

        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == "#" and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))




for _ in range(N):

    R, C = map(int, input().split())

    arr = [list(input()) for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]

    ans = 0

    for r in range(R):
        for c in range(C):
            if arr[r][c] == "#" and not visited[r][c]:
                bfs(r, c, R, C)
                ans += 1
    
    print(ans)

