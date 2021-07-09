# 할인된 상품 가격 출력
def product():
    product = {'쌀':9900, '상추':1900,'고추':2900,
               '마늘':8900,'통닭':5600,
               '햄':6900, '치즈':3900}
    return product


def computeDiscount(dp):
    p = product()

    for k, v in p.items():
        # price = v - (v * dp/100)
        price = v * (1 - (dp/100))
        print(f'{k:3s}\t {v:,d}원\t {dp} %DC -> {price:,.1f} 원')
        #포맷문자 형식이며, /t는 8칸 간격 띄우기

header = '-' * 40
header += '\n-- 한빛마트 오늘의할인 가격표 출력 시스템 --\n'
header += '-' * 40

print(header)
dp = float(input('오늘의 할인율을 입력하세요 '))

computeDiscount(dp)