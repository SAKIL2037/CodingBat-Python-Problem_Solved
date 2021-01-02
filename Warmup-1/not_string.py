def not_string(str):
  temp = str.split()
  if temp[0] == 'not':
    return str
  else:
    return 'not '+str
