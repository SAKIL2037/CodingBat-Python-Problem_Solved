def sum67(nums):
    sum = 0
    temp = 0
    for n in nums:
        if n == 6:
            temp = 1
            continue
        elif temp == 1:
            if n == 7:
                temp = 0
                continue
        else:
            sum = sum + n

    return sum

