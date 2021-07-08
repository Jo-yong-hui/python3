# 구매상품 할인율 계산
# 1개 - 5%
# 2개 - 10%
# 3개 - 20%
# 4개이상 - 30%
goods = []
flag = True

def checkDiscount(goods):
    rate = 0.3
    sum = 0

    if len(goods) == 1:
        rate = 0.05
    elif len(goods) == 2:
        rate = 0.1
    elif len(goods) == 3:
        rate = 0.2

    for i in range(len(goods)):
        sum += goods[i]

    fare = sum - (sum * rate)

    print(f'할인율 : {rate}')
    print(f'총구매금액 : {sum}')
    print(f'할인적용 구매금액 : {fare}')


def discountGoods():
    goods = []
    flag = True

    while flag:
        job = input('원하시는 작업을 선택하세요\n'
                    '1.구매 2. 종료')

        if job == '1':
            price = int(input('구매한 상품의 금액을 입력하세요 '))
            goods.append(price)

        elif job == '2':
            flag = False
            checkDiscount(goods)

        else:
            print('잘못입력하셨습니다!!')



