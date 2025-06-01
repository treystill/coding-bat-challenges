def has22(nums):
  for num in range(len(nums) - 1):
    if nums[num] == 2 and nums[num + 1] == 2:
      return True
  return False
