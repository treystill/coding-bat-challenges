def count_code(str):
  code = 0
  for index in range(len(str) - 3):
    if str[index:index + 2] == "co" and str[index + 3] == 'e':
      code = code + 1
    elif str[index:index + 5] == 'code':
      code = code + 1
  return code
  
"""
code
0123
"""