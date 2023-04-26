import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230412 6497 전력난

# 정답코드


def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def merge(x, y):

    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


while True:

    
    M, N = map(int, input().split())
    
    if M == 0 and N == 0:
        break

    parent = [i for i in range(M + 1)]

    edges = []
    ans = 0

    for _ in range(N):
        node1, node2, cost = map(int, input().split())
        ans += cost
        edges.append((cost, node1, node2))

    edges.sort()


    for i in range(N):
        cost, node1, node2 = edges[i]

        if find(node1) != find(node2):
            merge(node1, node2)
            ans -= cost


    print(ans)