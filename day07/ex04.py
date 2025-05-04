result = 0
num = int(input("请输入一个正整数："))
while num // 10 != 0:
    result = result *10 + num % 10 * 10
    num = num // 10
result = result  + num % 10
print(result)
