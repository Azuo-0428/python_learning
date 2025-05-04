"""
1. 定义总钱数1000元
2. 判断剩余钱数>0
3. 玩家下注,判断下注金额是否合理
4. 随机生成点数
5. 判断如果点数和如果是7或者11，玩家赢钱，若点数和为2或者3或者11，玩家扣钱，若点数和为其他值，进行下一轮
6. 再随机生成一轮，若和第一回点数和相同，则赢钱，若等于7则扣钱，否则继续往下循环
7. 这一次的结果和剩余钱数叠加，判断是否游戏结束
"""
import random

money = 1000
bet = 0
while money > 0:
    bet = float(input(f'您当前的本金为{money}，请玩家对本轮游戏进行下注：'))
    while bet > money or bet <=0:
        bet = float(input(f'您输入的赌注大于本金{money}，请重新下注：'))
    first_point = random.randrange(1, 7)
    second_point = random.randrange(1, 7)
    total_point = first_point + second_point
    print(first_point, second_point, total_point)
    if total_point == 7 or total_point == 11:
        money = money + bet
    elif total_point == 2 or total_point == 3 or total_point == 12:
        money = money - bet
    else:
        total_point1 = 0
        while total_point1 != total_point:
            total_point1 = total_point
            first_point = random.randrange(1, 7)
            second_point = random.randrange(1, 7)
            total_point = first_point + second_point
            print(first_point, second_point, total_point)
            if total_point ==7:
                money = money - bet
                break
            elif total_point == total_point1:
                money = money + bet
            else:
                continue
print('您的本金已无，游戏结束')

