def xyz_there(str):
  for index in range(len(str) - 1):
    if str[index: index + 3] == 'xyz':
      if str[index - 1] != '.':
        return True
  return False
