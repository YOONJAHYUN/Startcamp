import random

# 1~45 숫자를 담은 list 생성
# range(n,m) = n부터 m-1까지의 숫자를 생성

numbers = list(range(1,46))
# numbers가 가진 숫자 중에 무작위 값을 하나씩 6번 뽑기
# list가 가지고 있는 값 중 무작위 값을 뽑는 법은?
# print(random.chice(numbers))

# while문을 사용하여 뽑아보기

# n=1
# while n <= 6:
#     print(random.choice(numbers))
#     n += 1

print(random.sample(numbers,6))