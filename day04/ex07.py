"""

输入年份，闰年输入True，平年输出False

"""

year = int(input('请输入年份'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 ==0
print(f'{is_leap = }')