def make_ends(nums):
  if len(nums) >=1:
    temp = []
    temp.insert(0,nums[0])
    temp.insert(1,nums[len(nums)-1])
    return temp
