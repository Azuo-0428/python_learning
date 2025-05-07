"""

列表生成式

"""

# 创建一个取值范围在1到99且能够被3或者5整除的数字构成的列表
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

# 有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方
nums1 = [35, 12, 97, 64, 55]
# for num in nums1,遍历每一个nums1的元素
nums2 = [num ** 2 for num in nums1]
print(nums2)

# 有一个整数列表nums1，创建一个新的列表nums3，将nums1中大于50的元素放到nums2中
nums3=[num for num in nums1 if num > 50]
print(nums3)

