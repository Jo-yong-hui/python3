import keyword
# 한문장씩 출력 alt + shift + E
myName = '길동'
myMajor = '데이터 분석'



print(myName)
print(myMajor)



myName = 100
myName = True
myName = False
myName = 3.141519

intro = 'Hello'
print(intro)

intro = '안녕하세요.'
print(intro)

nickname = 'Mr.bucks'
print(nickname)

print(keyword.kwlist)
# print(keyword.softkwlist) # v3.9 추가

myName = 'park'

# $myScore = 111
# *score! = 999
_score_ = 99

bigint = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
print(bigint)

# 16자리만 찍혀서 나옴
bigfloat = 1.2345678901234567890
print(bigfloat)

a = 123
b = '456'

a = a + 1
b = b + 1

#어떤 자료형 타입인지 출력
print(type('안녕하세요'))
print(type(123))
print(type(True))

print(type(myName))

type('Hello Python')
type(123)
type(3.14)
type(True)

# 다중 선언: 서로다른 변수에 같은 값 선언
x = 1
y = 1
z = 1

x = y = z = 10

# 자릿수 구분: , 대신 _(언더바)로 쓸 수 있음
million = 1000000
million = 1_000_000
num=1_2_3

# 논리값 확인 : bool
bool(True)
bool(1) # 1이상 true
bool(100)
bool(-100)
bool(0) # 0이면 false

# 숫자를 문자형으로 변환
str(123)

# 문자를 숫자형으로 변환
int('456')

# 문자를 실수로 변환
float('3.14')

var1 = 123
var2 = var1
print(var1)
print(var2)

#\n 유무 차이는 입력이 가로, 세로로 됨
name = input('이름을 입력하세요\n')

print(name)

# 이름. 국어, 영어, 수학을 입력받아 출력하는 프로그램

name = input('이름을 입력하세요')
kor = input('국어?')
eng = input('영어?')
mat = input('수학?')

print('이름 : ', name)
print('국어 : ', kor)
print('영어 : ', eng)
print('수학 : ', mat)


