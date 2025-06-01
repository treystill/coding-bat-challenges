def centered_average(nums):
  center = sum(nums) - max(nums) - min(nums)
  return center / (len(nums) - 2)