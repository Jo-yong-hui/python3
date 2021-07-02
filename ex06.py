# 근무시간에 필요한 컴퓨터 수량

hour = int(input('근무시간을 입력하세요 '))

computer = 3 * 8 // hour
addCom = 1 if (3 * 8 % hour) > 0 else 0
print(f'필요한 컴퓨터수 : {computer + addCom}')

