num_1 = int(input('请输入一个正整数：'))
num_2 = int(input('请再输入一个正整数：'))
if num_1 < num_2:
    n = num_1
else:
    n = num_2
for i in range(1, n + 1):
    if num_1 % i != 0 or num_2 % i != 0:
        continue
    else:
        m = i
print(f'{m}是{num_1}和{num_2}的最大公约数')
