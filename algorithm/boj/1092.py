import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230513 1092 배

# 정답코드

N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

# 못 옮김
if boxes[0] > cranes[0]:
    print(-1)
    exit()

cnt = [0 for _ in range(N)]

for box in boxes:
    # idx: 사용할 크레인 번호 / temp: 크레인 사용 횟수(가장 무거운 것부터)
    idx, temp = 0, cnt[0]
    # 가장 용량 큰 크레인부터
    for i in range(N):
        # 옮길 수 있는 경우
        if box <= cranes[i]:
            # 선택한 크레인 사용 횟수가 더 적은 경우 (한번에 최대한 많은 크레인을 사용)
            if cnt[i] <= temp:
                # 크레인 선택
                idx = i 
                # 해당 크레인 사용횟수 저장
                temp = cnt[i]

        # 더이상 못 옮길 경우
        else:
            break
    
    # 해당 크레인 사용해서 박스 옮기기
    cnt[idx] += 1


print(max(cnt))
