def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0: # 짝수일 때
            arr = arr[:query[i]+1]
        else: # 홀수일 때
            arr = arr[query[i]:]
    return arr