import numpy as np
import consts as c

def jansky_to_mag(flux, ref_dist, new_dist=10):
  app_mag = -2.5 * np.log10(flux / 3631.)
  dist_mod = -5 * np.log10(ref_dist / new_dist)
  return app_mag + dist_mod
