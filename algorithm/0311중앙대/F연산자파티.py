import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230311 F 연산자파티

# 정답코드

N = int(input())
op = list(map(int, input().split()))

ans = 0

for i in range(1, N + 1):
    if i % op[0] == 0:
        ans += i
    if i % op[1] == 0:
        ans %= i
    if i % op[2] == 0:
        ans &= i
    if i % op[3] == 0:
        ans ^= i
    if i % op[4] == 0:
        ans |= i
    if i % op[5] == 0:
        ans >>= i

print(ans)