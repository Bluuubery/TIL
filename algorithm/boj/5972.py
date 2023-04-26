import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230425

# 택배배송

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cow, node = heapq.heappop(queue)

        if distance[node] == cow:
            for next in graph[node]:
                cost = distance[node] + next[1]
                if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(queue, (cost, next[0]))



V, E = map(int, input().split())
distance = [float("INF") for _ in range(V + 1)]

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    node1, node2, cow = map(int, input().split())
    graph[node1].append((node2, cow))
    graph[node2].append((node1, cow))

dijkstra(1)

print(distance[V])