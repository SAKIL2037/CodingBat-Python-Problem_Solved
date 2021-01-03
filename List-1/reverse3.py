def reverse3(nums):
    temp = []
    temp.insert(1, nums[1])
    temp.insert(0, nums[2])
    temp.insert(2, nums[0])

    return temp
