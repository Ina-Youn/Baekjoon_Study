import sys

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)] # 각 랜선의 길이

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0 # 랜선 개수
    for i in lan:
        lines += i // mid # 랜선 분할 시 나오는 개수
        
    if lines >= N: # 필요한 양 보다 더 많은 랜선이 나오는 경우
        start = mid + 1
    else:
        end = mid - 1
print(end)