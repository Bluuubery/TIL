from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230425 1516 게임개발

# 정답코드

N = int(input())

time = [0 for _ in range(N + 1)]

indegree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(N):
    temp = list(map(int, input().split()))
    
    time[i + 1] = temp[0]
    
    if len(time) > 2:
        for j in range(1, len(temp) - 1):
            graph[temp[j]].append(i + 1)
            indegree[i + 1] += 1




queue = deque()
answer = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    answer[current] += time[current]

    for next in graph[current]:
        indegree[next] -= 1
        answer[next] = max(answer[current], answer[next])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(answer[i])
