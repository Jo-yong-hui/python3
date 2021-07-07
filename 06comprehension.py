# 컴프리헨션comprehension
# 반복문 축약
# 파이션에는 4가지 축약을 지원
# list(py2) set, dict, generator(py3)


# 다양한 데이터 객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능


# 1 ~ 10까지 정수를 리스트에 저장
numlist = []
for i in range(1,10+1):
    numlist.append(i)
print(numlist)

# for 축약문
# [ 표현식 for 항목 in 반복가능객체 ]
numlist2 = [ i for i in range(1,10+1)]

# ex) 0 - 20사이 짝수를 리스트로 저장
evenlist = []
for i in range(1,10+1):
    numlist.append(i*2)

evenlist2 = [ i*2 for i in range(1,10+1)]

# ex) 1 - 10사이 제곱수를 리스트로 저장
sqllist = []
for i in range(1,10+1):
    sqllist.append(i*i)

sqllist2 = [ i ** 2 for i in range(1,10+1)]

# ex) 다음 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트로 생성하세요

val = [1, 2, 'A', False, 9, 100]
sqrlist3 = [ v**2 for v in val]

sqrlist3 = []
for v in val:
    if type(v) == int:       # 요소의 유형이 숫자라면
        sqrlist3.append(v ** 2)

# for if 축약문
# [ 표현식 for 항목 in 반복가능객체 if 조건 ]
sqrlist4 = [ v ** 2 for v in val if type(v) == int ]

# ex) 1 - 50사이 홀수를 리스트로 저장
oddlist = [ i for i in range(1, 50+1) if i % 2 != 0]


# 다중조건을 사용하는 for 축약문
# [ 표현식1 if 조건 els 표현식2 for 항목 in 반복가능객체 ]

# ex) 1 - 100사이 정수 중 임의의 숫자가 짝수면 'even',
#     홀수면 'odd'로 구분해서 리스트로 저장
evenodd = [ 'even' if i % 2 == 0 else 'odd'
            for i in range(1, 100+1) ]

# 중첩 for 문을 사용하는 for 축약문
# [ 표현식 for 항목1 in 반복가능객체1
#         for 항목2 in 반복가능객체2 ]

# ex) 구구단 중 7단, 8단 계산값을 리스트에 저장
gugu = []
for i in range(7, 8+1):
    for j in range(1, 9+1):
        gugu.append(i * j)
        gugu
gugu2 = [i * j for i in range(7, 8+1)
               for j in range(1, 9+1) ]

# ex) 1 ~ 100 사이의 제곱수가 아닌 수를
# 찾아서 리스트로 생성 ( 제안: sqrt()함수 사용)


from math import sqrt

# 제곱수 : sqrt(4) % 1
# 제곱수 아님 : sqrt(5) % 1

square = [ i for i in range(1,100+1)
           if sqrt(i) % 1 != 0 ]

