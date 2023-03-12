from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230311 중앙대 B 시프트연산

# 정답코드

N = int(input())

arr = list(map(int, input().split()))

arr = deque(arr)

def shift_left():
    arr.rotate(-1)
    arr[-1] = 0

def shif_right():
    arr.rotate()
    arr[0] = 0

min_move = 0
ans = ""

left = 0
right = N - 1

while True:
    
    if left > right:
        break


    if arr[left]:
        for i in range(left + 1):
            shift_left()
            min_move += 1
            ans += "L"
            print(ans, min_move, arr, left, right)
        left = 0
        right = N - 1

    elif arr[right]:
        for i in range(N - right):
            shif_right()
            min_move += 1
            ans += "R"
            print(ans, min_move, arr, left, right)
        left = 0
        right = N - 1
    else:
        left += 1
        right -= 1


print(min_move)
print(ans)