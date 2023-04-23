import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230416 b 사격내기

# 정답코드

A, B = map(int, input().split())

scores = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

def find_score(total):

    result = set()

    while total > 0:

        for score in scores:
            if total >= score:
                result.add(score)
                total -= score
                break
        
    return result

A_score = find_score(A)
B_score = find_score(B)

C_score = set.symmetric_difference(A_score, B_score)

print(sum(C_score))