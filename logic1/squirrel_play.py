def squirrel_play(temp, is_summer):
  if 60 <= temp <= 100 and is_summer:
    return True
  elif 60 <= temp <= 90:
    return True
  return False