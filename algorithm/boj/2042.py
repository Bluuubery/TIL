import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230606 2042 구간 합 구하기

# 정답코드

def init(node, start, end):

    # 리프노드
    if start == end: 
        tree[node] = numbers[start]

    # 좌우 자식 트리의 합 재귀적으로 더해서 저장
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)

    return tree[node]



def query(node, start, end, left, right):

    # 범위 벗어남
    if left > end or right < start:
        return 0

    # 범위내에 들어가는 경우 해당 구간합 바로 반환
    if left <= start and end <= right:
        return tree[node]
    
    # 좌우 자식 트리의 합(구간합) 더해서 반환
    return query(node * 2, start, (start + end) // 2, left, right) + query(node * 2 + 1, (start + end) // 2 + 1, end, left, right)



def update(node, start, end, idx, val):
    
    # 범위 벗어난 경우
    if idx < start or idx > end:
        return
    
    # 리프노드
    numbers[idx] = val
    tree[node] = val

    # 부모 노드 재귀적으로 업데이트
    if start != end:
        update(node * 2, start, (start + end) // 2, idx, val)
        update(node * 2 + 1, (start + end) // 2 + 1, end, idx, val)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]




N, M, K = map(int, input().split())
numbers = []
tree = [0 for _ in range(3000000)]


for _ in range(N):
    numbers.append(int(input()))

init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        b -= 1
        update(1, 0, N - 1, b, c)
    else:
        print(query(1, 0, N - 1, b - 1, c - 1))


