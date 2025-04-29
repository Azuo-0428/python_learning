""""

变量的类型转换

"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello world'
g = True
print(float(a))
print(int(b))
print(int(c))
print(int(c, base=16))  # 将16进制转换为10进制
print(int(d, base=2))
print(float(e))
print(bool(f))  # 只要字符串有内容，就是true
print(int(g))
print(chr(a))  # 将整数转换成字符串
print(ord('d'))  # 将字符串转换成对应整数
