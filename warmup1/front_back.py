def front_back(str):
  if len(str) > 1:
    length = len(str) 
    return str[length - 1:length] + str[1:length - 1] + str[0]
  else:
    return str