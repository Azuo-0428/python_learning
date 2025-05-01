""""

升级版BMI计算器

"""

weight = float(input('体重（kg）：'))
height = float(input('身高（cm）：'))
BMI = weight / (height / 100) ** 2
print(f'{BMI = :.1f}')
if BMI < 18.5:
    print('你的体重过轻！')
elif 18.5 <= BMI < 24:
    print('你的身材很棒！')
elif BMI < 27:
    print('你的体重过重！')
elif BMI <30:
    print('你已轻度肥胖！')
elif BMI <35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')
