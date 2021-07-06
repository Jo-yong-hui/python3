# 369 게임만들기 배수로 간단하게 써본것
for i in range(1,100):
    clap = ''  # clap 초기화
    if i % 3 == 0 or i % 6 == 0 or i % 9 == 0:
        clap = "짝"
    print(f'{i} {clap}')

# 369 게임만들기
for i in range(1,100):
    clap=''
    if i < 10:              # 숫자가 한자리라면
        if i % 3 == 0:
            clap = "짝!"
    else:                   # 숫자가 두자리라면     ex)34
        num1 = i // 10      # 첫째 숫자 추출(몫)     ex)3
        num2 = i % 10       # 나머지 숫자 추출       ex)4

        if num1 % 3 == 0:    # 첫째 숫자가 3의 배수라면
            clap += '짝!'

        if num2 % 3 == 0 and num2 != 0:   # 둘째 숫자가 3의 배수이고, 0이 아니라면
            clap += "짝!"

    print(f'{i} {clap}', end=',')
print()
# 미국판 369 게임 - buzz
# https://www.wikihow.com/Play-Buzz

# 로그인 기능 만들기
