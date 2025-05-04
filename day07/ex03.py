# 1.从100循环到100
# 2.

for i in range(100, 1000):
    j = i % 100
    k = j % 10
    l = j // 10
    m = i // 100
    if i == k ** 3 + l **3 + m**3:
        print(i)
    else:
        continue
