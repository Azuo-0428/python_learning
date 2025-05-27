"""

大小写变换

"""

s1 = 'hello, world'
# 字符串首字母大写
print(s1.capitalize())
# 字符串每个单词首字母大写
print(s1.title())
# 字符串变大写
print(s1.upper())
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())
# 检查s1和s2的值
print(s1)
print(s2)

"""

查找操作

"""

s = 'hello world!'
print(s.find('or'))
print(s.rfind('o'))
print(s.rindex('o'))

s1 = 'goodbye world'
s2 = 'I am not happy'
print(s2.find('o'))
print(s2.rfind('o'))
print(s2.rindex('o'))

"""

性质判断

"""

s1 = 'hello, world!'
print(s1.startswith('He'))  # 以He开头
print(s1.startswith('he'))
print(s1.endswith('!'))  # 以！结尾
s2 = 'abc123456'
print(s2.isdigit())  # 全部由数字组成
print(s2.isalpha())  # 全部由字母构成
print(s2.isalnum())  # 由数字和字母组成

"""

格式化

"""

s = 'hello, world!'
print(s.center(20, '*'))
print(s.ljust(20, '~'))
print(s.rjust(20, '^'))
print('33'.zfill(5))  # 左侧补零
print('-33'.zfill(5))

a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')
