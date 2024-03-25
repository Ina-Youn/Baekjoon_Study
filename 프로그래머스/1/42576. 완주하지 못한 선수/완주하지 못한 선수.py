def solution(participant, completion):

    participant.sort() # 참가자(완주자 + 1)
    completion.sort() # 완주자
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]