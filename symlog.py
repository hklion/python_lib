import numpy as np

def symlog(xmax, n=100, linthresh=1., linscale=1., endpoint=True, verbose=False):
  n = n - 1
  if (endpoint == False):
    n += 1
  decades = np.log10(xmax / linthresh)
  n_half = n // 2
  n_per_dec = n_half / (decades + linscale)
  n_lin = int(linscale * n_per_dec)
  n_log = int(decades * n_per_dec)
  n_mod = n_half % int(n_lin + n_log) #number of bins left over
  if verbose:
    print(n_per_dec, n_lin, n_log, n_mod, (n_lin + n_log)*2)

  # distribute remaining extra bins between lin and log, porportionally
  lin_frac = n_lin / (n_lin + n_log)
  lin_xtra = int(lin_frac * n_mod)
  log_xtra = n_mod - lin_xtra

  n_lin += lin_xtra
  n_log += log_xtra

  if verbose:
    print(lin_xtra, log_xtra)
    print(n_per_dec, n_lin, n_log, n_mod, (n_lin + n_log)*2)
  all_lin = np.linspace(-linthresh, linthresh, n_lin * 2 + 1 + n % 2, endpoint=True)[:-1]

  pos_log = np.logspace(np.log10(linthresh), np.log10(xmax), n_log+1, endpoint=True)
  neg_log = -pos_log[1:][::-1]

  symlog = np.concatenate((neg_log, all_lin, pos_log))
  if (endpoint == False):
    symlog = symlog[:-1]
  if verbose:
    print(symlog)
    print(len(symlog))

  return symlog
