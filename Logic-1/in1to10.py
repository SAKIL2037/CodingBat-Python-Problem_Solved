def in1to10(n, outside_mode):
  if outside_mode == False:
    if 1 <= n <= 10:
     return True
    else:
      return False
  elif 1 < n < 10:
    return False
  else:
    return True
