def centered_average(nums):
    nums.sort()
    count = 0
    sum = 0
    for n in nums[1:len(nums) - 1]:
        sum = sum + n
        count = count + 1

    return sum / count
