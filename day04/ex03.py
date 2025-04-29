"""

赋值运算符和符合赋值运算符

"""

a = 10
b = 3
a += b  # a = a+b
a *= a + 2  # a = a * (a+ 2)
print(a)

"""

海象运算符

"""

# SyntaxError: invalid syntax
# print((b = 10))
# 海象运算符
print((b := 10))
print(b)
