# 元组和列表创建时间

# timeit函数看创建保存元素花费时间
import timeit

print('%.3f 秒' % timeit.timeit('[1,2,3,4,5,6,7,8,9]', number=10000000))
print('%3f 秒' % timeit.timeit('(1,2,3,4,5,6,7,8,9)', number=10000000))
