def sum13(nums):
    sum = 0
    temp = 0
    if nums == [] or nums == [13]:
        return 0
    else:
        for n in nums:
            if n == 13:
                temp = n
                continue
            elif temp == 13:
                temp = 0
                continue
            else:
                sum = sum + n

    return sum
