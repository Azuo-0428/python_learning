"""

列表的嵌套，列表的元素是列表

"""

# 保存5个学生的3门课程成绩
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
# 第一个学生的第二门成绩
print(scores[0][1])
# 如果想通过键盘输入的方式录入五个学生3门课程的成绩，并且保存在列表中
scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score = int(input('请输入：'))
        temp.append(score)
    scores.append(temp)
print(scores)
# 通过产生随机数的方式生成5个学生3门课程的成绩，并且保存在列表中
import random
scores = [[random.randrange(60,101) for _ in range(3)] for _ in range(5)]
print(scores)