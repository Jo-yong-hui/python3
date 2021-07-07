# 수학시험 프로그램

# quiz = ['3+2?','5÷2의 몫?','10-2?','10²x2?',
#        '1-(10÷4의 나머지)','2²?','4÷2?']
# answer = [5,2,8,200,-1,16,2]
# point = [3,5,3,5,5,3,3]
#
# # asw = []
# # cnt = len(quiz)
# # for i in range(cnt):
# #     print(f'문제 {quiz[i]}')
# #     asw.append(input('정답을 입력하세요 '))
# #
# # good = 0
# # jumsu = 0
# # for i in range(cnt):
# #     if int(asw[i]) == answer[i]:
# #         good += 1
# #         jumsu += point[i]
#
# cnt = len(quiz)
# good = 0
# jumsu = 0
#
# for i in range(cnt):
#     print(f'문제 {quiz[i]}')
#     asw = input('정답을 입력하세요 ')
#
#     if int(asw) == answer[i]:
#         good += 1
#         jumsu += point[i]
#
#
# print('-'*30)
# print(f'정답 갯수 : {good}\n'
#       f'오답 갯수 : {cnt - good}\n'
#       f'총 점수 : {jumsu}')
# print('-'*30)


quiz = [['3+2?',5,3], ['5÷2의 몫?',2,5], ['10-2?',8,3],
        ['10²x2?',200,5], ['1-(10÷4의 나머지)',-1,5],
        ['2²?',16,3], ['4÷2?',2,3]]

cnt = len(quiz)
good = 0
jumsu = 0

for q in quiz:
    print(f'문제 {q[0]}')
    asw = input('정답을 입력하세요 ')

    if int(asw) == q[1]:
        good += 1
        jumsu += q[2]

print('-'*30)
print(f'정답 갯수 : {good}\n'
      f'오답 갯수 : {cnt - good}\n'
      f'총 점수 : {jumsu}')
print('-'*30)