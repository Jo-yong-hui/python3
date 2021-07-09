# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시 코드가 섞이지 않게
# 하기 위한 목적도 있음 - 모듈


def startSensor():
    print('온도센서 작동을 시작한다')


def stopSensor():
    print('온도센서 작동을 중지한다')

startSensor()
stopSensor()


# 노트북 파우치 인치 변환
# 1cm -> 0.393701 inch

def convertCM2inch(cm):
    print(f'{cm * 0.393701:.2f}')
    # return cm * 0.393701

cm = int(input('파우치 길이를 입력하세요 '))
convertCM2inch(cm)
# print(convertCM2inch(cm))


# 이동거리 계산
def computeDistance(time, speed):
    print(f'이동 거리는 {time * speed} km 입니다')

time = float(input('이동 시간은? '))
speed = float(input('이동 속도는? '))
computeDistance(time, speed)


def add():
    print(a + b)


a = input('a는? ')
b = input('b는? ')


add()   # add 호출하는 방식

# 웹사이트 방문 누적하기
count = 10

def countVisitor():   # 함수정의
    global count  # 위  전역변수 10 그대로 사용한다. (위 10사용할떈 재설정 할 필요 없다.)
    # global count = 0 # 전역변수는 초기화 불가,
    count = 0
    while True:
        menu = input('1.웹사이트 방문 2.종료\n'
                     '작업을 선택하세요')
        if menu == '1':
            count += 1
            print(f'총 방문 횟수: {count} ' )
        elif menu == '2':
             break

print(f'전체 방문횟수 {count}')

countVisitor() # 함수 호출


x = 10
y = 10

def add():
    print(x + y)

def add(x, y):
    print(x + y)

add()
add(10,10)

# 함수의 매개변수 갯수를 동적으로 정의
# 매개변수명 앞에 *로 정의해서 함수를 만들면 됨

# ex) 기존에 만든 add 함수는 2개의 매개변수만 받음
# 2개이상의 매개변수를 받아 결과를 출력하고 싶다면?
def add(x,y,z):
    print(x + y + z)

def add2(*num):
    sum = 0
    for v in num:
        sum += v
        print(sum)
add2(10,10)
add2(10,10,10,10)
add2(10,10,10,10,10,10,10,10)


## MMS/SMS 구분하기
def computeMS(msg):
    msgSize = len(msg)
    print('입력하신 문자열 길이', msgSize)

    if msgSize <= 100:
        print(f'단문 메시지로 50원이 부과됩니다' )

    elif msgSize > 100:
        print(f'장문 메시지로 100원이 부과됩니다' )

msg = input('문자열을 입력하세요')
computeMS(msg)


# 함수정의시 매개변수를 선언했지만
# 함수호출시 인수를 순서대로 입력하지 않을 경우
# => 인수값 앞에 매개변수명을 지정

def computeSungJuk(name, kor, eng, mat):
    tot = kor + eng + mat
    avg = tot / 3
    print(tot, avg)
    

computeSungJuk('혜교',99,98,87)
computeSungJuk(99,98,87,'수지')   # 오류발생!
computeSungJuk(96,99,87, name='박수')  # 오류발생!

computeSungJuk(kor=96,eng=99,mat=87, name='박수') # 변수 같이 사용하면 가능
computeSungJuk(name=87,kor=96,eng=99,mat=87)   # 변수 같이 사용하면 가능

# 매개변수를 정의했지만
# 매개변수 없이 함수 호출하고 싶다면?
# -> 매개변수 선언시 초기값을 지정함

def add3(x=10, y=10):
    print(x + y)

add3(5, 5)

add3()


#사칙연산 프로그램
def compute(x,y):
    add = x + y
    min = x - y
    mul = x * y
    div = x / y

    return add, min, mul, div # 각각 자리수 마다 p, m, c, d 순서로 변수가 넘어감

num1 = int(input('첫번째 정수를 입력하세요' ))
num2 = int(input('첫번째 정수를 입력하세요' ))
p, m, c, d = compute(num1, num2)
result = compute(num1, num2)

print(f'사칙연산 결과 : ({p},{m},{c},{d:.2f})')
print(f'사칙연산 결과 : {result}')





