"""

每隔一秒输出一次“hello world”，持续1小时

"""

import time  # time 模块可以实现程序休眠

for i in range(3600):  # 从0到3599
    print('hello world')
    time.sleep(1)
