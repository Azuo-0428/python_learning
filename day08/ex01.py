"""

掷6000次骰子，记录每个点数出现的次数

"""

import random

i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
for _ in range(1, 6001):
    point = random.randrange(1, 7)
    if point == 1:
        i += 1
    elif point == 2:
        j += 1
    elif point == 3:
        k += 1
    elif point == 4:
        l += 1
    elif point == 5:
        m += 1
    else:
        n += 1
print(f'点数为1的出现次数有{i}，点数为2的出现次数有{j}，点数为3的出现次数有{k}，点数为4的出现次数有{l}，点数为5的出现次数有{m}，点数为6的出现次数有{n}')
