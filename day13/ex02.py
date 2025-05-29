"""

字典的key

"""

person = {
    'name':'阿张',
    'age': 28,
    'height':182,
    'weight':80,
    'addr':['上海市','北京市'],
    'car':{
        'brand':'BMW X7',
        'maxSpeed': '250',
        'length':5170,
        'width':2000,
        'height':1835,
        'displacement':3.0
    }
}
print(person)


# 成员运算
print('name' in person)
print('tel' in person)

# 索引运算
print(person['name'])