# 4. 이걸 1000번 반복한다.
    # 1. 로또 번호 6개 추천받는다.
    # 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
        # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서
            # 1049회 당첨번호 목록에 해당 숫자가 있는지
            # numbers = [1, 2, 3, 4, 5]
            # if 3 in numbers:
                # print(true)


            # 있다면 적중 횟수 + 1

    # 그래서 적중 횟수가 6개면 1등
    # 5개면 3등
    # 4개면 4등
    # 3개면 5등
    # 2개이하면 꽝을 출력한다.


import random






date = input('회차를 입력해 주세요  : ')

import requests

r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={date}').json()


num = (r['drwtNo1'], r['drwtNo2'], r['drwtNo3'], r['drwtNo4'], r['drwtNo5'], r['drwtNo6'])
print(num)


numbers = list(range(1,46))
for x in range(1000):
    a = random.sample(numbers,6)
    print(a)
    count =0
    for i in a:
        if i in num:
            count += 1

    if count == 6:
        print('1등')
    elif count == 5:
        print('3등')
    elif count == 4:
        print('4등')
    elif count == 3:
        print('5등')
    else:
        print('꽝')