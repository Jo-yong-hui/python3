
# 패키지 package

# 함수, 클래스들을 용도별로 분리해서
# 작성하는 것을 모듈이라 했음

# 그런데, 이러한 모듈들이 모여 뒤죽박죽 섞여 있으면
# 이해도, 활용도가 떨어질수 있음


# 따라서, 모듈들 역시 성격에 맞게 분류해서 관리해야 할
# 필요성이 대두 - 패키지를 이용해서 모듈들을 관리
# 파이썬에서는 패키지를 만들려면

# 디렉토리 생성 -> __init__.py 파일 생성하면 됨
# python3 이상 __init__.py 를 만들지 않아도
# 패키지로 인식
# => python2와의 호환을 위해 생성할 것을 권장


# 모듈 불러오기
# import 패키지명.모듈파일명 순서로 작성

import module.calculator

# 정의한 모듈의 특정 기능을 사용하려면
# '패키지명 모둘명 함수명'으로 호출
module.calculator.add(3, 5)

module.calculator.minus(10, 4)

module.calculator.multiply(12, 3)

module.calculator.devide(10, 3)

# 단위 변환 프로그램
import module.ConvertUnit

data = int(input('변환할 길이(mm)를 입력하세요'))

result = module.ConvertUnit.convertLength(data)
module.ConvertUnit.printUnits(result)


# 시험 합격여부
import module.exam

kor = int(input('국어는? '))
eng = int(input('영어는? '))
mat = int(input('수학은? '))
tot, avg, ispass = module.exam.exampass(kor, eng, mat)

print(f'총점 : {tot}\n평균 : {avg:.2f} \n합격여부 : {ispass}')


# 모듈명 줄여쓰기 : as
import module.calculator as mcc
import module.ConvertUnit as mcu
import module.exam as me

mcc.add(3,5)
mcc.multiply(3,5)
mcu.convertLength(20)
me.exampass(54,65,76)

# 모듈중에서 특정 함수만 사용하고 싶을때는
# from 패키지명.
# 모듈명 import 함수명' 형식을 사용

from module.calculator import add
from module.calculator import devide  # (가독성을 위해 추천)

from module.calculator import add, devide


# 수학모듈
import math as m

print(m.ceil(10.5))
print(m.ceil(10.1))
print(m.floor(10.9))
print(m.floor(10.1))

import random as r
print(r.random())  # 랜덤은 0이상 ~ 1미만 사이 실수
print(r.randint(1,45)) # 1 ~ 45
print(r.randrange(1,45)) # 1 ~ 44
print(r.sample(range(1,10),3)) # 1하고 10사이 임의의 숫자 3개 표본추출
print(r.choice(range(1,10)))  # 무작위로 1개 추출

# 점심메뉴 추천 프로그램
lunches = ['갈비탕','돈까스','김밥','김치찌개','뼈해장국',
           '부대찌개','햄버거','쌀국수','짜장면','탕수육']

idx1 = r.sample(range(10), 1)[0]
idx2 = r.randint(0,9)  # - randint() : 정수 난수 생성
idx3 = r.randrange(0,10) # 지정한 범위(첫 항으로부터 공차를 더하여 최대점을 넘지 않는 범위)의 정수 난수 생성
idx4 = r.choice(range(10)) # 지정된 범위에서 무작위 1개 추출

print(f'오늘의 점심메뉴는 {lunches[idx1]}')
print(f'오늘의 점심메뉴는 {lunches[idx2]}')
print(f'오늘의 점심메뉴는 {lunches[idx3]}')
print(f'오늘의 점심메뉴는 {lunches[idx4]}')

import time as t
print(t.time())
print(t.localtime()) # 요일(wday)은 월요일을 기준으로 0 ~ 7

fmt = '%Y-%m-%d %H:%M:%S'
print(t.strftime(fmt, t.localtime()))

print('카운트다운을 시작합니다')
t.sleep(1)  # 1초 동안 실행 대기
print(5)
t.sleep(1)
print(4)
t.sleep(1)
print(3)
t.sleep(1)
print(2)
t.sleep(1)
print(1)
t.sleep(1)
print(0)


# 구매 상품 할인율 적용
from module.DcGoods import discountGoods

discountGoods()

# 로또 당첨 프로그램
from module.Lotto645 import Lotto654

Lotto654()