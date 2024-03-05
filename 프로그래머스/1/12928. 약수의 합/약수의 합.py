def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        # n % i 가 0일 경우, i는 n의 약수 
        if n % i == 0:
            # 약수 i를 answer값에 더하기
            answer += i
    return answer