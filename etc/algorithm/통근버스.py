import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

N = int(input())
bus = list(map(int, input().split()))

arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for j in range(N - 1, -1, -1):
    for x in range(1, N + 1):
        arr[x][j] = arr[x][j + 1] + (1 if bus[j] < x else 0)

ans = 0
for i in range(N):
    for j in range(N):
        if bus[i] < bus[j]:
            ans += arr[bus[i]][j]

print(ans)