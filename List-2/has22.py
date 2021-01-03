def has22(nums):
    temp = True
    if len(nums) < 2:
        return False
    else:
        for i in range(len(nums) - 1):
            if nums[i] == 2 and nums[i + 1] == 2:
                return True
            else:
                temp = False

    return temp


