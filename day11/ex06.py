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
print(s3.replace('o', '@'))
print(s3.replace('o', '@', 1))

"""

拆分与合并

"""

s4 = 'I love you so much'
words = s4.split()  # 将一个字符串拆成多个字符串（放在同一列表中）
print(words)
print('~'.join(words))
print('#'.join(words))
words1 = s4.split('#')
print(words1)
s5 = 'I#love#you#so#much'
words2 = s5.split('#', 2)
print(words2)

"""

编码和解码

"""

a = '阿左'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)
print(c)
print(b.decode('utf-8'))
print(c.decode('gbk'))