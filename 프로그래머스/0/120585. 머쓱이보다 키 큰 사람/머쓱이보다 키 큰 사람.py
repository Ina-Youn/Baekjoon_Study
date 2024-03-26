def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
        else:
            answer = 0
    return answer