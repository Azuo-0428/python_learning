"""

CRAPS 赌博游戏摇色子获得点数的功能封装到函数中

"""
from random import randrange

# 表示默认值是2
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
        return total

# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
print(roll_dice(3))
