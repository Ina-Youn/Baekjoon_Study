def solution(n):
    # 2진수로 변환했을 때 1의 갯수 확인
    cnt = bin(n).count('1') # bin(숫자) -> 해당 숫자를 2진수로 변환하는 함수
    while 1:
        n += 1
        if bin(n).count('1') == cnt:
            return n