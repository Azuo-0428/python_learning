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