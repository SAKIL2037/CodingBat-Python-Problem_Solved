def near_ten(num):
  temp = num%10
  if num%10==0 or num%10 == 1 or num%10==2:
    return True
  elif abs(temp - 10) == 1 or abs(temp - 10) == 2:
    return True
  else:
    return False
