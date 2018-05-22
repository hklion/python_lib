import numpy as np

def num_format(num):
  if num == 0.0:
    return '0.0e0'
  exp = int(np.log10(num))
  remainder = num / (10 ** exp)
  if exp <= 0 and remainder < 1:
    exp = exp - 1
    remainder = num / (10 ** exp)
  round_remainder = round(remainder, 2)
  return str(round_remainder) + 'e' + str(exp) 
