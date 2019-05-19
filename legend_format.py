import matplotlib.pyplot as plt
import matplotlib.lines as mlines

blank_line = mlines.Line2D([],[],color='none',label='')

def format_handles(handle_list, cols=[1], align='up'):
  if len(cols) == 1:
    return handle_list
  assert len(handle_list) > 0
  assert len(handle_list) == sum(cols)

  original_len = len(handle_list)
  max_col_len = max(cols)
  final_len = max(cols) * len(cols)
  i_handle = 0
  i_col = 0
  for i, col_size in enumerate(cols):
    n_blanks = max_col_len - col_size
    if align == 'up':
      for blank in range(n_blanks):
        handle_list.insert(i * max_col_len + col_size, blank_line)
    elif align == 'down':
      for blank in range(n_blanks):
        handle_list.insert(i * max_col_len, blank_line)
  return handle_list


