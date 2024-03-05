def solution(babbling):
    
    # 아기가 발음할 수 있는 단어
    say = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling:
        for j in say:
            i = i.replace(j, '*')
            
        if i.replace('*', '') == '':
            answer += 1
    
    return answer