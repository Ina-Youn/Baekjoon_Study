import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
# 입력 받은 배열 정렬
# 입력 받은 배열 중 중복 제거
# 순서대로 정렬
arr2 = sorted(list(set(arr)))

# 정렬 한 좌표와 인덱스를 dic에 저장
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=' ')