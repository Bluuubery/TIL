from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230116 차세대 지능형 교통 시스템

# 정답코드

dir_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


traffic_dict = {
    1 : ('up', 'right', 'down'),
    2 : ('left', 'up', 'right'),
    3 : ('up', 'left', 'down'),
    4 : ('left', 'down', 'right'),
    5 : ('up', 'right'),
    6 : ('left', 'up'),
    7 : ('left', 'down'),
    8 : ('down', 'right'),
    9 : ('right', 'down'),
    10 : ('up', 'right'),
    11 : ('up', 'left'),
    12 : ('left', 'down')
}


can_go_dict = {
    'right' : (1, 5, 9),
    'up' : (2, 6, 10),
    'left' : (3, 7, 11),
    'down': (4, 8, 12)
}


N, T = map(int, input().split())

traffic_input = dict()

for i in range(N):
    for j in range(N):
        traffic_input[(i, j)] = list(map(int, input().split()))


check = set()
ans = set()
queue = deque()

time = 0
dir = 'up'

queue.append([0, 0, time, dir])
check.add((0, 0, time, dir))
ans.add((0, 0))

while queue:
    r, c, time, dir = queue.popleft() # 0, 0, 0, 'up'

    can_go = can_go_dict[dir] # (2, 6, 10)
    traffic = traffic_input[(r, c)][time % 4] # 2

    if traffic in can_go: 
        for d in traffic_dict[traffic]: # ('left', 'up', 'right)
            dr, dc = dir_dict[d]

            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N and (nr, nc, time + 1, d) not in check:
                if time + 1 <= T:
                    print(nr, nc, time + 1, d)
                    ans.add((nr, nc))
                    check.add((nr, nc, time + 1, d))
                    queue.append([nr, nc, time + 1, d])

print(len(ans))