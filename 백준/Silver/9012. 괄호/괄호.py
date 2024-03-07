### 1st

T = int(input()) # 테스트 데이터의 수

for _ in range(T): # 테스트 데이터 만큼 반복
    i = input() # 입력 받은 테스트 데이터
    while i.find('()') != -1: # find 함수를 통해 '()' 문자열이 처음으로 나온 위치를 확인한다. '()'가 없을 경우 -1이 반환된다.
        i = i.replace('()', '') # '()' 문자열을 ''로 바꾼다.
    print('YES' if len(i) == 0 else 'NO') # 입력 받은 테스트 데이터의 길이가 0이 될 경우 'YES', 아닐 경우 'NO' 출력

### 2nd

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
