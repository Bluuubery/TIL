import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230426 16956 늑대와 양

# 정답코드

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

for r in range(R):
    for c in range(C):
        if arr[r][c] == ".":
            arr[r][c] = 'D'

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve():
    global R, C

    for r in range(R):
        for c in range(C):
            if arr[r][c] == 'W':
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C:
                        if arr[nr][nc] == 'S':
                            print(0)
                            return
    
    print(1)
    for row in arr:
        print(*row, sep='')
    return

solve()
