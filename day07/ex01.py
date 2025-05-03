"""

100以内的素数

"""
for i in range(2, 100):
    for j in range(2, i + 1):
        n = i % j
        if n == 0 and j != i:
            break
        elif n == 0 and j == i:
            print(i)

"""

for num in range(2, 100):
    is prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(num)

"""
