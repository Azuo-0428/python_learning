# 打包操作
a = 10, 4, 78, 98, 97
print(type(a))
print(a)

# 解包操作
x, y, z, k, j = a
print(x, y, z, k, j)

# 变量个数少于元素的个数,星号只能出现一次
x, y, z, *k = a
print(x, y, z, k)
x, y, *z = a
print(x, y, z)
*x, y, z = a
print(x, y, z)

a, *b, c = range(1, 9)
print(a, b, c)
a, b, c = [1, 3, 4]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)
