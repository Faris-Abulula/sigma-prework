def maxmin(nums):
    max = nums[0]
    min = nums[0]
    for num in nums:
        if num > max:
            max = num
        elif num < min:
            min = num
    return [min, max]

print(maxmin([2, 4, 1, 0, 2, -1]))
print(maxmin([20, 50, 12, 6, 14, 8]))
print(maxmin([100, -100]))