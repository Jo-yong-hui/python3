# 수심에 따른 수온 계산

depth = int(input('수심을 입력하세요 '))
temp = 20
temp = temp - (depth // 10 * 0.7)
print(f'수온: {temp}')




