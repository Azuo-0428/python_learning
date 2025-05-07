"""

双色球随机选号程序

"""

import random

red_balls = list(range(1, 34))
selected_balls = []
# 添加6个红色球到选中列表
for _ in range(6):
    # 生成随机整数代表选中的红色球的索引位置
    index = random.randrange(len(red_balls))
    # 将选中的球从红色球列表中移除并且添加到选中列表中
    selected_balls.append(red_balls.pop(index))
# 对选中的红色球进行排序
red_balls.sort()
# 输出选中的红球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end=' ')
# 随机选择1个蓝球
blue_ball = random.randrange(1,17)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')

# sample 无放回随机抽样和 choice 随机取一个函数
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
selected_balls = random.sample(red_balls,6)
selected_balls.sort()
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end=' ')
blue_ball = random.choice(blue_balls)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

# 随机生成N注号码
n = int(input('生成几注号码：'))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
for _ in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    blue_ball = random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')