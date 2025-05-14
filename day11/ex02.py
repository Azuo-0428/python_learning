"""

转义字符

"""
s1 = '\'hello, world\''
print(s1)
s2 = '\\hello,world\\'
print(s2)

"""
原始字符串

"""
s3 = '\it \is \time \to \read \now'
s4 = r'\it \is \time \to \read \now'
print(s3)
print(s4)

"""

字符的特殊表示

"""

s5 = '\141\142\143\x61\x62\x63'
s6 = '\u9a86\u660a'
print(s5)
print(s6)
