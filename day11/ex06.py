"""

修剪操作

"""
s1 = '   azuoyizuo@gmial.com   '
print(s1)
print(s1.strip())  # 默认修剪空格
s2 = '~你好，世界~'
print(s2)
print(s2.lstrip('~'))
print(s2.rstrip('~'))

"""

替换操作

"""

s3 = 'hello, good world!'
print(s3.replace('o','@'))
print(s3.replace('o','@',1))

"""

拆分与合并

"""

s4 = 'I love you'
words = s4.split() #将一个字符串拆成多个字符串（放在同一列表中）
print(words)
print('~'.join(words))
