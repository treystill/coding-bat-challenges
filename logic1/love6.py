def love6(a, b):
  sum = a + b
  dif = a - b
  if a == 6 or b == 6:
    return True
  elif sum == 6 or abs(dif) == 6:
    return True 
  return False
