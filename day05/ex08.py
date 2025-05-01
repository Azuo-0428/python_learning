a = float(input('请输入三角形的边长：'))
b = float(input('请输入三角形的边长：'))
c = float(input('请输入三角形的边长：'))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'{perimeter = }')
    s = perimeter / 2
    Area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'{Area = }')
else:
    print('不能构成三角形')
