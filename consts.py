import numpy as np

# Physical constants (cgs)
c = 2.99792458e10
h = 6.6260755e-27
hbar = h / (2. * np.pi)
ggrav = 6.67259e-8
e = 4.8032068e-10
me = 9.1093897e-28
mp = 1.6726231e-24
mn = 1.6749286e-24
mh = 1.6733e-24
amu = 1.6605402e-24
na = 6.0221367e23 # Avogadro's number
kb = 1.380658e-16
ev = 1.6021772e-12
a = 7.5646e-15 # Radiation density constant
sb = 5.67051e-5 # Stefan-Boltzmann constant
alpha = 7.29735308e-3 # Fine structure
ryd = 2.1798741e-11 # Rydberg constant

# Astrophysical constants (cgs)
au = 1.496e13
pc = 3.086e18
ly = 9.463e17
msun = 1.99e33
rsun = 6.96e10
rearth = 6.3781e8
lsun = 3.9e33
teffsun = 5.78e3

cm_per_m = msun * ggrav / c ** 2
s_per_m = cm_per_m / c
