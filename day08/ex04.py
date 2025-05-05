"""

索引运算

"""

items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])
print(items8[2])
print(items8[4])
items8[2] = 'durian'
print(items8)
print(items8[-5])
print(items8[-4])
print(items8[-1])
items8[-4] = 'strawberry'
print(items8)
print(items8[1:3:1])
print(items8[0:3:1])
print(items8[0:5:2])
print(items8[-4:-2:1])
print(items8[-2:-6:-1])
print(items8[1:3])
print(items8[:3:1])
print(items8[::2])
print(items8[-4:-2])
print(items8[-2::-1])
items8[1: 3] = ['x', 'o']
print(items8)
