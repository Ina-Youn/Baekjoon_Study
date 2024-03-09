### 1st

T=int(input())

for i in range(T):
    string = list(input().split())
    for j in string:
        print(j[::-1],end=' ')

### 2nd
for _ in range(int(input())):
    print(' '.join([i[::-1] for i in input().split()]))
