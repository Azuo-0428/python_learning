"""

从1到100偶数求和

"""

total = 0
for i in range(1,101):
    if i % 2 != 0:
        continue  #放弃本次循环直接进入下一轮循环
    total +=i
print(total)