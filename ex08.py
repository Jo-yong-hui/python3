# 차량 2부제 프로그램
# day = input('오늘 날짜는? ')
from datetime import datetime as dt
day = dt.now().day
day = dt.today().day


car = input('차량번호는? ')

evenOrodd = '짝수'
if int(day) % 2 != 0: evenOrodd = '홀수'
print(f'오늘 입차 : 번호가 {evenOrodd}인 차량')

passOrNot = '입차 불가'
#if int(car) % 2 == 0 and int(day) % 2 != 0: # 검사 2번시행
if int(car) % 2 == 0 and evenOrodd == '짝수':
    passOrNot = '입차 가능'
print(f'귀하의 차량은 {passOrNot}합니다')
