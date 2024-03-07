T = int(input())

for _ in range(T):
    i = input()
    while i.find('()') != -1:
        i = i.replace('()', '')
    print('YES' if len(i) == 0 else 'NO')