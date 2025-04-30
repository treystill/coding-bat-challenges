def alarm_clock(day, vacation):
  if day == 1 and vacation or day == 2 and vacation or day == 3 and vacation or day == 4 and vacation or day == 5 and vacation:
    return str('10:00')
  elif day == 0 and vacation or day == 6 and vacation:
    return str('off')
  elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    return str('7:00')
  elif day == 0 or day == 6:
    return str('10:00')