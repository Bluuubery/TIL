import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230521 b 준석이의 사탕 사기

# 정답코드

N = int(input())

numbers = list(map(int, input().split()))

odd = sorted(list(filter(lambda x : x % 2, numbers)), reverse= True)
even = list(filter(lambda x: x % 2 == 0, numbers))

ans = sum(even)

if len(odd) >= 2:
    ans += sum(odd)
    if len(odd) % 2:
        ans -= odd[-1]

print(ans)
