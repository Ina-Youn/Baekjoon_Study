from collections import deque

def solution(people, limit):
    count = 0 # 구명보트의 수
    people = deque(sorted(people))
    
    # 모든 사람이 구출될 때 까지
    while people:
        person = people.pop() # 몸무게가 가장 많이 나가는 사람
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()
            
        count += 1
    return count