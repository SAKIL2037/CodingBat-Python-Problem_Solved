def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        sum = 0
        for num in nums:
            sum = sum + num
        return sum

    else:
        return nums[0] + nums[1]
