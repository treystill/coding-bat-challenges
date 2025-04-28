def extra_end(str):
  if len(str) > 2:
    l = len(str)
    return str[l-2:l] + str[l-2:l] + str[l-2:l]
  else:
    return str + str + str
