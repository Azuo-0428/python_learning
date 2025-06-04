"""

判断三条边的长度是否可以构成三角形

"""


def make_judgement(a, b, c):
    return a + b > c and b + c > a and a + c > b


print(make_judgement(1, 2, 3))
print(make_judgement(4, 5, 6))

print(make_judgement(b=5, c=4, a=3))
