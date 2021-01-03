def array123(nums):
    temp = [1, 2, 3]
    bln = False
    for i in range(len(nums) - 2):
        if temp == nums[i:i + 3]:
            bln = True

    return bln