"""

字典的key

"""

person = {
    'name': '阿张',
    'age': 28,
    'height': 182,
    'weight': 80,
    'addr': ['上海市', '北京市'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)

# 成员运算
print('name' in person)
print('tel' in person)

# 索引运算
print(person['name'])
print(person['addr'])
person['age'] = 30
person['height'] = 178
person['tel'] = 17896587412
person['signature'] = '慢即是快'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')

# 返回默认值
print(person.get('name'))
print(person.get('hobby'))
print(person.get('sex',True))

# 获取key and value
print(person.keys())
print(person.values())
print(person.items())
for key, value in person.items():
    print(f'{key}:\t{value}')

# 两个字典的合并
person2 = {'name':'隔壁老王', 'age':}