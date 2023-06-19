import math
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230611 14438 수열과 쿼리 17

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
        

N = int(input())
A = list(map(int, input().split()))
height = math.ceil(math.log2(N))
tree_size = 1 << (height+1)
tree = [0] * tree_size

init(A, tree, 1, 0, N-1)
m = int(input())
for _ in range(m):
    what, t1, t2 = map(int, input().split())
    if what == 1:
        index, val = t1, t2
        update(A, tree, 1, 0, N-1, index-1, val)
    else:
        left, right = t1, t2
        print(query(tree, 1, 0, N-1, left-1, right-1))
