nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
total = 0
count = 0
while count < len(nums):
    if nums[count] % 2 == 0:
        total += nums[count]
    count += 1
print(total)


