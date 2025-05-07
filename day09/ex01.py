"""

删除和添加元素

"""

languages = ['Python', 'Java', 'C++']
languages.append('Javascript')
print(languages)
languages.insert(1, 'SQL')
print(languages)
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)
# pop()删掉最后一个元素
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.append('Python')
print(languages)
languages.remove('Python')
print(languages)
# del不会返回删除元素，pop会返回
del languages[1]
print(languages)
items = ['SQL', 'JavaScript', 'Java']
languages += items
languages.append('Python')
print(languages)
print(languages.index('Java'))
print(languages.index('Python'))
print(languages.count('Python'))
print(languages.count('Java'))
print(languages.index('SQL',2))
languages.sort()
print(languages)
languages.reverse()
print(languages)
