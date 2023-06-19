import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230617 7662 이중 우선순위 큐

# 정답코드


T = int(input())

for _ in range(T):

    K = int(input())

    max_heap = []
    min_heap = []
    check = [False for _ in range(K)]

    for id in range(K):
        op, number = input().split()
        number = int(number)

        if op == "I":
            heapq.heappush(min_heap, (number, id))
            heapq.heappush(max_heap, (-number, id))
            check[id] = True
        
        else:
            if number == 1:
                while max_heap:
                    number, id = heapq.heappop(max_heap)
                    if check[id]:
                        check[id] = False
                        break

            else:
                while min_heap:
                    number, id = heapq.heappop(min_heap)
                    if check[id]:
                        check[id] = False
                        break
        # print(max_heap)
        # print(min_heap)
        # print()
    
    while max_heap and not check[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    while min_heap and not check[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap:
        # print(max_heap)
        # print(min_heap)
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")