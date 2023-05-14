import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230514 20165 인내의 도미노 장인 호석

# 정답코드

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


ans = 0
board = [["S" for _ in range(M)] for _ in range(N)]
dir = {
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
    "N": (-1, 0)
}


# 수비
def defense(X:int, Y:int) -> None:

    board[X][Y] = "S"

    return


# 공격: 주어진 방향으로의 블럭들을 재귀적으로 넘어뜨리는 함수
def attack(X:int, Y:int, D:str) -> None:
    global ans

    # 이미 넘어진 블럭
    if board[X][Y] == "F":
        return
    
    # 넘어뜨리기
    board[X][Y] = "F"
    ans += 1

    # 주어진 방향으로 높이 만큼의 블럭들 재귀적으로 넘어뜨린다 
    height = arr[X][Y]
    for i in range(1, height):
        nX = X + dir[D][0] * i
        nY = Y + dir[D][1] * i
        if 0 <= nX < N and 0 <= nY < M:
            attack(nX, nY, D)

    return
    



for r in range(R * 2):

    if r % 2:
        X, Y = map(int, input().split())
        defense(X - 1, Y - 1)

    else:
        X, Y, D = input().split()
        X = int(X)
        Y = int(Y)
        attack(X - 1, Y - 1, D)



print(ans)
for row in board:
    print(*row)
