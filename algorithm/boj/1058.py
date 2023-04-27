import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230427 1058 친구

# 정답코드

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    relationship = list(input())
    for j in range(N):
        if relationship[j] == "Y":
            graph[i].append(j)

max_friend = 0
for current in range(N):

    # 중복
    check = set()

    # 한다리 거쳐서
    for next in graph[current]:
        
        # 바로 연결
        check.add((current, next))

        for next_next in graph[next]:

            if next_next == current:
                continue

            check.add((current, next_next))


    max_friend = max(max_friend, len(check))

print(max_friend)

