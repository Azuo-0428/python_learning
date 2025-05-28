"""

集合的方法

"""

set1 = {1, 10, 100}
# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)  # remove方法若元素不存在，会引发KeyError
print(set1)

# 清空元素
set1.clear()
print(set1)

# 判断是否由相同元素
set1 = {'Java','Python','C++','Kotlin'}
set2 = {'Kotlin','Swift','Java','Dart'}
set3 = {'HTML','CSS', 'JavaScript'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
