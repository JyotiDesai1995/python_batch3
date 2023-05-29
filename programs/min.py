nums = [66, 88, 23, 999, 17, 456]
min_num = nums[0]
for num in nums:
    if num > min_num:
        min_num = num

print("Max number is:", min_num)
