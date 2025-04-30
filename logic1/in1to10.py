def in1to10(n, outside_mode):
  if outside_mode and n <= 1 or outside_mode and n >= 10:
    return True
  elif outside_mode == False and 1 <= n <= 10:
    return True 
  return False
