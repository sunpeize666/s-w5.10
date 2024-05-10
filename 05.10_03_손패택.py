'''
2024년05월10일
202195057 손패택
'''
import random

num = []

for i in range(10):
    num.append(random.randint(1,100))

print("생성된 리스트 : ",num)
print("최대값 : ",max(num))
print("최소값 : ",min(num))
print("합게 : ",sum(num))

num.sort()
print("오름치순 정럴 : ",num)