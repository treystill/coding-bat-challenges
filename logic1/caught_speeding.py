def caught_speeding(speed, is_birthday):
  if speed <= 65 and is_birthday:
    return 0
  elif 66 <= speed <= 85 and is_birthday:
    return 1
  elif speed >= 86 and is_birthday:
    return 2
  if speed <= 60:
    return 0
  elif 61 <= speed <= 80:
    return 1
  elif speed >= 81:
    return 2