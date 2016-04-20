import numpy as np

# Counts number of lines in a file
def nlines(fname):
  with open(fname) as f:
    n = sum(1 for line in f)
  return n

# Unlogging not working right. Ignoring for now.
def unlog(data):
  new_names = []
  for name in data.dtype.names:
    if name[:3] == 'log' or name[:3] == 'Log':
      # Strip off 'log' in field name
      if name[3] == '_':
        new_name = name[4:]
      else:
        new_name = name[3:]
      new_names.append(new_name)
    else:
      new_names.append(name)
  data.dtype.names = tuple(new_names)

def load_header(fname, labelrow, do_unlog=False):
  header = labelrow - 1
  footer = nlines(fname) - (labelrow + 2)
  data = np.genfromtxt(fname, skip_header = header, skip_footer = footer, 
      names = True)
  if do_unlog:
    data = unlog(data)
  return data

def load_array(fname, labelrow, do_unlog=False):
  header = labelrow - 1
  data = np.genfromtxt(fname, skip_header = header, names=True)
  if do_unlog:
    data = unlog(data)
  return data
