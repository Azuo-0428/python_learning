# 定义一个三元组
t1 = (28, 19, 22)
t2 = ('阿左', 35, True, '上海')

# 查看变量类型
print(type(t1))
print(type(t2))

# 查看元组中的元素数量
print(len(t1))
print(len(t2))

# 索引运算
print(t1[0])
print(t2[2])
print(t2[-1])

# 切片运算
print(t1[:2])
print(t2[::3])

# 循环遍历元组中的元素
for i in t2:
    print(i)

# 成员运算
print(19 in t1)
print(12 in t2)
print('zuo' not in t2)

# 拼接运算
t3 = t1 + t2
print(t3)

# 比较运算
print(t1 == t3)
print(t1 != t2)
print(t1 <= t3)
print(t1 <= (31, 67, 100))
