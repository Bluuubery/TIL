import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230529 17393 다이나믹 롤러

# 정답 코드

N = int(input())
ink_list = list(map(int, input().split()))
viscosity_list = list(map(int, input().split()))

answer = []

for i in range(N):
    ink = ink_list[i]
    res = i

    start = i + 1
    end = N - 1
    mid = 0

    while True:

        if start > end:
            break

        mid = (start + end) // 2

        if ink < viscosity_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
            res = mid
    
    answer.append(res - i)

print(*answer)
