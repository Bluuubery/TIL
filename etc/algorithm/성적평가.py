import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 210115 성적평가

# 정답코드

def get_rank(score:list):
    score = list(enumerate(score))
    score.sort(key= lambda x:x[1], reverse=True)

    result = [0 for _ in range(N)]
    result[score[0][0]] = 1

    rank = 1
    cnt = 1

    for i in range(1, N):
        if score[i][1] == score[i - 1][1]:
            cnt += 1
        
        else:
            rank += cnt
            cnt = 1
        
        result[score[i][0]] = rank

    print(*result)


N = int(input())
total_score = [0 for _ in range(N)]

for _ in range(3):
    score_list = list(map(int, input().split()))

    for i in range(N):
        total_score[i] += score_list[i]

    get_rank(score_list)

get_rank(total_score)



