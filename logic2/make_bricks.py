def make_bricks(small, big, goal):
  bigs = big * 5
  if small >= goal or bigs >= goal or small + bigs >= goal:
   return True
  return False