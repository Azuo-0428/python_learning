"""

BMI 计算器

"""

height = float(input('身高（cm）：'))
weight = float(input('体重（kg）：'))
BMI = weight / (height / 100) ** 2
print(f'{BMI = :.1f}')
if 18.5 <= BMI < 24:
    print('你的身材很棒！')
else :
    print('你的身材不够标准哟！')