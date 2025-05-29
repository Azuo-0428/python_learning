"""

创建和使用字典

"""

xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区；南~货，外~货；种类：他俩是一~人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '上海市',
    'tel': '12345678910',
    'emergence contact': '98765432101'
}
print(person)

# dict函数（构造器）
person = dict(name='阿张', age=28, height=182, weight=80, addr='上海市')
print(person)

# python 内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)

# 键值对个数和对字典遍历
person1 = {
    'name':'阿辉',
    'age': 28,
    'height':182,
    'weight':80,
    'addr':'上海'
}
print(len(person1))
for key in person:    # for 只对key进行遍历
    print(key)