import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230419 17451 평행우주

# 정답코드

N = int(input())

planets = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    
    if planets[i - 1] < planets[i]:
        
        k = planets[i] // planets[i - 1] if planets[i]%planets[i - 1] == 0 else planets[i] // planets[i - 1] + 1
        
        planets[i - 1] *= k

print(planets[0])
