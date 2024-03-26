# mode: 0으로 시작, code 문자가 '1'일 경우 mode 변경
# mode가 0일때: 문자가 1이 아니면, idx-짝수 일 때만 ret에 추가
# mode가 1일때: 문자가 1이 아니면, idx-홀수 일 때만 ret에 추가
# ret가 빈 문자열일 경우 'EMPTY' return

# abc1abc1abc
# 012345678910
# acbac

def solution(code):
    mode = 0
    answer = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                answer += code[i]
            elif code[i] == '1':
                mode = 1
        else:
            if code[i] != '1' and i % 2 == 1:
                answer += code[i]
            elif code[i] == '1':
                mode = 0
    if answer == '':
        return 'EMPTY'
    return answer