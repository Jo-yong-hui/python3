# if문 - 콜론 입력후, 엔터를쳐서 들여쓰기로 작성해야 한다.
# (num > 10) 여기서 괄호해도되고 안해도 된다.

# num = int(input('숫자를 하나 입력하세요'))
# if num > 10:
#     print('num은 10보다 크다')
#
#
# # 속도위반 경고 : 50km/h
# speed = int(input('자동차의 현재 속도는? '))
# # if speed > 50:
# #     print('속도위반!!')
#
# if speed > 50: print('속도위반!!')

# 합격/불합격 출력 : if ~ else
# score = int(input('점수를 입력하세요 '))
#
# if (score >= 80):
#     print('합격입니다')
# else:
#     print('아쉽습니다. 다시 도전해주세요~')


# 실행문이 아직 정해지지 않는 경우 pass 키워드로 대체 작성 가능
# if (score >= 80):
#     pass
# else:
#     pass


# temp = int(input('온도는?'))
# if ( temp >= 40 ):
#     print('Fan 가동')
# else:
#     print('Fan 중지')
    
# 입력받은 정수를 3으로 나눠 소수점 첫째자리가 0.5이상인 경우
# 반올림해서 출력하고 그렇지 않은 경우 그대로 출력하는 프로그램
# num = int(input('정수를 하나 입력하세요 '))
#
# result = num / 3
# if (result - int(result) >= 0.5):
#     result = int(result) + 1 # 소수이하자리 버린후 올림
# else:
#     result = int(result)     # 소수이하자리만 버림
# print(f'결과 : {result}')

# mileage = int(input('마일리지를 입력하세요'))
#
# if mileage >= 1000:
#     print('마일리지 사용가능')
# else:
#     print('마일리지 사용불가')

# 성적처리

# jumsu = int(input('점수를 입력하세요 '))
#
# if 60 <= jumsu < 70:
#     print('양')
# elif 70 <= jumsu < 80:
#     print('미')
# elif 80 <= jumsu < 90:
#     print('우')
# elif 90 <= jumsu <= 100:
#     print('수')
# else:
#     print('가')

# 자동주문 시스템 만들기
intro = '안녕하세요, 만나서 반갑습니다\n'\
      '어디서 오셨나요? 다음 번호를 선택하세요\n'\
      '1.대한민국 2.USA 3.中國'
nation = input(intro)

if (nation == '1'):
    intro = '주문하시겠어요?'
elif (nation == '2'):
    intro = 'Would you like to order?'
elif (nation == '3'):
    intro = '您要点菜吗?'
else:
    intro = 'Would you like to order?'

print(intro)

# 국가재난지원금 수령액 조회
# 출력표시방법 : f'{money:,}여기안에 콤마와 _, .1f써서 표시가능
count = int(input('인원수를 입력하세요 '))

if count == 1:
    money = 400_000
elif count == 2:
    money = 600_000
elif count == 3:
    money = 800_000
else:
    money = 1_000_000
print(f'{money:,.1f}원 지원')

# BMI 지수를 계산하고 그에 따른 다양한 결과 출력
# < 18.5: 저체중
# < 23 : 정상
# < 25 : 과체중
# < 30 : 비만
# > 30 : 고도비만

weight = int(input('몸무게는? '))
height = int(input('신장은? '))
height = height / 100

bmi = weight / (height * height)

if bmi > 30: print('고도 비만')
elif bmi > 25: print('비만')
elif bmi > 23: print('과체중')
elif bmi > 18.5: print('정상체중')
else: print('저체중')

# 버스 전용차로 단속 
msg = '1.월~금, 2.토요일, 3.공휴일\n'\
      '요일을 선택하세요 (1~3)'
day = input(msg)

if day == '1':
    msg = '버스 전용차로 단속중입니다'
else:
    msg = '토요일 및 공휴일은 단속하지 않습니다'
print(msg)

msg = '1.버스 2.승용차\n'\
      '차종을 선택하세요 (1~2)'
car = input(msg)

if car == '1':
    msg = '버스입니다 - 단속대상 아님'
elif car == '2':
    if day == '1':
        msg = '버스 전용차로 위반!!'
    else:
        msg = '승용차입니다 - 단속대상 아님'
print(msg)


# 공적 마스크 구매 가능 요일 계산
year = input('출생연도 끝자리는? ')
age = input('만 나이는? ')

day = ''
if int(age) < 65:
    if year == '1' or year == '6': day = '월'
    elif year == '2' or year == '7': day = '화'
    elif year == '3' or year == '8': day = '수'
    elif year == '4' or year == '9': day = '목'
    elif year == '5' or year == '0': day = '금'
    print(f'{day}요일에 구매 가능합니다')
else:
    print('언제든지 구매가능합니다!')

