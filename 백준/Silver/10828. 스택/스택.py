import sys
input = sys.stdin.readline
n=int(input())
stack=[]

for i in range(n):
    commend = input().split()
    if commend[0] == 'push':
        stack.append(commend[1])
    elif commend[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif commend[0] == 'size':
        print(len(stack))
    elif commend[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)