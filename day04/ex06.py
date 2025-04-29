"""

输入半径计算圆的周长和面积

"""

radius = float(input('请输入圆的半径：'))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长： %.2f' % perimeter)
print('面积： %.2f' % area)

import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长：{perimeter:.2f}')
print(f'面积{area: .2f}')

import math
radius = float(input('请输入圆的半径'))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')
print(f'{area = :.2f}')
