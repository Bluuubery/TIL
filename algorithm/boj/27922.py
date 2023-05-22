import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230522 27922 현대모비스 입사 프로젝트

# 정답코드

N, K = map(int, input().split())
lectures = [list(map(int, input().split())) for _ in range(N)]

ab = sum(sorted(list((lambda x: x[0] + x[1])(x) for x in lectures), reverse= True)[:K])
bc = sum(sorted(list((lambda x: x[1] + x[2])(x) for x in lectures), reverse= True)[:K])
ac = sum(sorted(list((lambda x: x[0] + x[2])(x) for x in lectures), reverse= True)[:K])

print(max(ab, bc, ac))
