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

s1 = 'hello, world'
s2 = 'goodbye world'
print('wo' in s1)
print('wo' not in s2)
print(s2 in s1)

s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('wo' not in s2)  # False
print(s2 in s1)        # False
