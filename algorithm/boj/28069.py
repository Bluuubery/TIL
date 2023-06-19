from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230619 28069 김밥천국의 계단

# 정답코드

N, K = map(int, input().split())

current = 0

visited = [0 for _ in range(N + 1)]

def bfs(curr, cnt):

    queue = deque()
    queue.append((curr, cnt))
    visited[curr] = 1

    while queue:

        curr, cnt = queue.popleft()
        # print(curr, cnt)

        if curr == N:
            print("minigimbob")
            return

        next_1 = curr + 1
        next_2 = curr + curr//2

        if next_1 <= N and cnt < K and not visited[next_1]:
            visited[next_1] = 1
            queue.append((next_1, cnt + 1))
        
        if next_2 <= N and cnt < K and not visited[next_2]:
            # print(next_2, cnt)
            visited[next_2] = 1
            queue.append((next_2, cnt + 1))
    
    print("water")
    return

bfs(0, 0)