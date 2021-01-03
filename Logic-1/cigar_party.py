def cigar_party(cigars, is_weekend):
  if is_weekend == True:
    if cigars >=40:
     return True
    else:
      return False
  elif 40<=cigars<=60:
    return True
  else:
    return False
