def cigar_party(cigars, is_weekend):
  if cigars <=  60 and cigars >= 40:
    return True
  if cigars > 40 and is_weekend:
    return True
  return False
