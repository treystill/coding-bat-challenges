def xyz_there(str):
  a = 0
  b = 0
  for index in range(len(str) - 1):
    if len(str) >= 3:
      if str[index: index + 3] == "xyz":
        a = a + 1
    if str[index: index + 4] == ".xyz":
      b = b + 1
      a = a - 1
  if len(str) >= 3 and a > 0 and a >= b:
    return True
  return False
