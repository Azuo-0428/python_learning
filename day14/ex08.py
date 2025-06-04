"""

可变位置参数实现对任意多个数求和的add函数

"""


# *表示arg可以接收0个或任意多个参数
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行类型检查
        if type(val) in (int, float):
            total += val
    return total


print(add())
print(add(1))
print(add(1, 2, 3))
print(add(1, 2, 'hello', 3.45, 6))


def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2, 1, True, name='rh', age=28, height=182)
