def max_end3(nums):
  if nums[0] > nums[2]:
    temp = []
    temp.insert(0,nums[0])
    temp.insert(1,nums[0])
    temp.insert(2,nums[0])
    return temp
  else:
    temp = []
    temp.insert(0,nums[2])
    temp.insert(1,nums[2])
    temp.insert(2,nums[2])
    return temp
