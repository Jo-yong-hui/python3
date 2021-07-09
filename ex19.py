# 계산기 프로그램

# def computer():
#     num1 = int(input('첫번째 숫자를 입력하세요 '))
#     op = input('1.덧셈 2.뺄샘 3.곱셈 4.나눗셈\n'
#                 '연산자를 선택하세요 ' )
#     num2 = int(input('두번째 숫자를 입력하세요 '))
#     compute(op, num1, num2)
#
#
# def compute(op, num1, num2):
#     if op == '1':
#         print(f'덧셈 결과 : {num1 + num2}')
#     elif op == '2':
#         print(f'뺄셈 결과 : {num1 - num2}')
#     elif op == '3':
#         print(f'곱셈 결과 : {num1 * num2}')
#     elif op == '4':
#         print(f'나눗셈 결과 : {num1 / num2}')
#     else:
#         print(f'연산자를 잘못 입력하셨어요')
#
# computer()

# 전역 global 변수와 지역 local 변수
# 전역변수보다 지역변수를 우선시 한다.
num = 10        # 10
print('전역변수 num', num)

def local():
    num = 20   # 20
    print('함수내 num', num)

local()

print('전역변수 num',num)   # 10

# 함수내에서 전역변수 사용하기 : global
num = 10       # 10
print('전역변수 num', num)

def local():
    global num     # 함수내에서 전역변수를 수정할 수 있도록 함
    num = 20 # 20
    print('함수내 num', num)

local()

print('전역변수 num', num) # 10(x) -> 20


# 웹사이트 방문 누적하기
count = 0

def countVisitor():
    pass

countVisitor()