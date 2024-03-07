import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
	a = input()
	stack = 0
	for i in a:
		if i == '(':
			stack +=1
		elif i == ')':
			stack -=1
			
		if stack < 0:
			break
			
	if stack == 0:
		print('YES')
	else:
		print('NO')