"""

二元运算

"""

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集 intersection
print(set1 & set2)
print(set1.intersection(set2))

# 并集 union
print(set1 | set2)
print(set1.union(set2))

# 差集 difference
print(set1 - set2)
print(set1.difference(set2))

# 对称差 symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

set3 = {1, 3, 5, 7}
set4 = {2, 4, 6}
set3 |= set4
print(set3)
set5 = {3, 6, 9}
set3 &= set5
print(set3)
set4 -= set3
print(set4)
