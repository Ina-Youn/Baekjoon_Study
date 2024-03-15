def solution(s):
    stack = []
    
    for i in range(len(s)):
        if not stack: # stack이 비어있을 경우
            stack.append(s[i])
        else:
            if s[i] == stack[-1]: # s[i]와 스택의 마지막 값이 같을 경우
                stack.pop()
            else: # s[i]와 스택의 마지막 값이 같지 않을 경우
                stack.append(s[i])
    if stack:
        return 0
    else:
        return 1