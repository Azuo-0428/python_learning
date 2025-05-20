"""

比较运算

"""

s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)
print(s1 >= s2)
print(s1 < s2)
print(s1 > s2)
print(s1 != s2)
s3 = '李琰'
s4 = '陆溓宁'
print(ord('李'))
print(ord('琰'))
print(ord('陆'))
print(ord('溓'))
print(ord('宁'))
print(s3 >= s4)
print(s3 != s4)

"""

成员运算

"""

s5 = 'hello, world'
s6 = 'goodbye world'
print('wo' in s5)
print('wo' not in s5)
print(s6 in s5)

"""

获取字符串长度

"""

s = 'hello, world'
print(len(s))
print(len('goodbye, world'))

"""

索引和切片

"""

s = 'abc123456'
n = len(s)
print(s[0], s[-1])
print(s[n - 1], s[-1])
print(s[2], s[7])
print(s[5], s[-4])
print(s[2:5])
print(s[-7:-4])
print(s[2:])
print(s[:2])
print(s[::2])
print(s[::-1])