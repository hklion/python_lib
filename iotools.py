import numpy as np

def num_format(num):
  exp = int(np.log10(num))
  remainder = num / (10 ** exp)
  if exp <= 0 and remainder < 1:
    exp = exp - 1
    remainder = num / (10 ** exp)
  round_remainder = round(remainder, 2)
  return str(round_remainder) + 'e' + str(exp) 
