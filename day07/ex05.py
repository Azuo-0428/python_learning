for i in range(0, 21):
    for j in range(0, 34):
        for k in range(0, 300):
            if 5 * i + 3 * j + k / 3 == 100 and i + j + k == 100 and k % 3 == 0:
                print(f'鸡翁的个数为{i}只，鸡母的个数为{j}只，雏鸡的个数为{k}只')
            else:
                continue
