import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230423 16562 친구비

# 정답코드

# find 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# union 함수
def merge(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
        
    else:
        parent[x] = y

    return

N, M, k = map(int, input().split())

parent = [i for i in range(N + 1)]
cost = [0] + list(map(int, input().split()))

edges = []

# 기존 친구
for _ in range(M):
    v, w = map(int, input().split())
    edges.append((0, v, w))

# 친구비
for i in range(1, N + 1):
    edges.append((cost[i], 0, i))

edges.sort()


ans = 0
cnt = 0
for e in edges:
    cost, friend1, friend2 = e

    if cost > k:
        break

    if find(friend1) != find(friend2):
        
        print(cost, friend1, friend2)
        merge(friend1, friend2)

        ans += cost
        k -= cost
        cnt += 1

if cnt < N:
    print("Oh no")
else:
    print(ans)

