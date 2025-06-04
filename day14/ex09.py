"""

命名冲突

"""


def foo():
    print('Hello, world!')


def foo():
    print('Goodbye world!')


print(foo())
