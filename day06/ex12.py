num = int(input('请输入一个正整数:'))
end = int(num ** 0.5)
is_prime = True
for i in range(2,end+1):
    if num % i ==0:
        is_prime = False
        break
if is_prime is True:
    print(f'{num}这是一个素数')
else:
    print(f'{num}这不是一个素数')
