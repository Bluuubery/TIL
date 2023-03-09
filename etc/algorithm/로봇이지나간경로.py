import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230116 로봇이 지나간 경로

# 정답코드

R, C = map(int, input().split())

board = [input() for _ in range(R)]

# 시작 지점 찾기

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dir_dict = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, -1): '<',
    (0, 1): '>'
}

def check_start(r, c):
    cnt = 0
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == '#':
                cnt += 1
                next_dir = (dr[i], dc[i])

    if cnt == 1:
        return (True, dir_dict[next_dir]) 

    return (False, [])
    

for r in range(R):
    for c in range(C):
        if board[r][c] == '#':
            if check_start(r, c)[0]:
                s_r, s_c = r, c
                dir = check_start(r, c)[1]
                break


# 이동 경로 찾기

ans = ''

visited = [[0 for _ in range(C)] for _ in range(R)]





