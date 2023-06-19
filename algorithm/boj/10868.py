import math
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230613 10868 최솟값

# 정답코드

def init(A, tree, node, start, end):

    if start == end:
        tree[node] = A[start]
    
    else:
        init(A, tree, node*2, start, (start + end) // 2)
        init(A, tree, node*2 + 1, (start + end)//2 + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def update(A, tree, node, start, end, idx, val):

    if idx < start or idx > end:
        return
    
    # 리프노드
    if start == end:
        A[idx] = val
        tree[node] = val
        return

    update(A, tree, node*2, start, (start + end) // 2, idx, val)
    update(A, tree, node*2 + 1, (start + end)//2 + 1, end, idx, val)
    tree[node] = min(tree[node * 2], tree[node*2 + 1])


def query(tree, node, start, end, left, right):
    
    if left > end or right < start:
        return -1
    
    if left <= start and end <= right:
        return tree[node]
    
    lmin = query(tree, node*2, start, (start + end) // 2, left, right)
    rmin = query(tree, node*2 + 1, (start + end)//2 + 1, end, left, right)
    
    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return min(lmin, rmin)
        

N, M = map(int, input().split())
A = list(int(input()) for _ in range(N))
height = math.ceil(math.log2(N))
tree_size = 1 << (height+1)
tree = [0] * tree_size

init(A, tree, 1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    print(query(tree, 1, 0, N - 1, a - 1, b - 1))
