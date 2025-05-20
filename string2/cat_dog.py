def cat_dog(str):
  this_is_dog = "dog"
  this_is_cat = "cat"
  cat = 0
  dog = 0
  for index in range(len(str) - 1):
    #if len(str) - 3 != index:
    if str[index:index + 3] == this_is_cat:
      cat = cat + 1
    elif str[index:index + 3] == this_is_dog:
      dog = dog + 1
  if cat == dog:
    return True
  return False
  