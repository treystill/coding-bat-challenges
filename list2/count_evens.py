def count_evens(nums):
  amount = 0
  for index in nums:
    if index % 2 == 0:
      amount = amount + 1
  return amount