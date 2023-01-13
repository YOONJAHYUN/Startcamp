# 파이썬으로 웹 요청 보낼수 있는 라이브러리 불러오기

# 동행복권 로또 당첨 번호 api 사용하기
# 회차 직접 입력
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호제외)

# 선택사항 : 보너스 번호 확인하기

import requests

date = input('회차를 입력해 주세요  : ')
print(date)

r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={date}').json()

print(date, '회차의 당첨 번호는', r['drwtNo1'], r['drwtNo2'], r['drwtNo3'], r['drwtNo4'], r['drwtNo5'], r['drwtNo6'], '입니다. \n그리고 보너스 번호는 ', r['bnusNo'], '입니다.')