def solution(quiz):
    answer = []
    ls = []
    
    for i in quiz:
        ls = i.split(' ')
        if ls[1] == '-':
            a = int(ls[0]) - int(ls[2])
            if a == int(ls[-1]):
                answer.append("O")
            else:
                answer.append("X")
        if ls[1] == '+':
            a = int(ls[0]) + int(ls[2])
            if a == int(ls[-1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
    return answer