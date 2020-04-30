from numpy import random
import numpy as np
import double_maxwellian

L = 100    # domain of solution 0 <= x <= L
N = 20000  # number of electrons
J = 1000   # number of grid points
vb = 3     # beam velocity
dt = 0.1   # time-step (in inverse plasma frequencies)
tmax = 80  # simulation run from t = 0 to t = tmax

#initialize solution
t = 0
np.rng(42)                              # seed the rand generator
r = L*random.uniform(0,1,N)             # electron positions
#dlmwrite('r.txt',r,'delimiter','\t','precision','%25.15e');
v = double_maxwellian(N,vb)             # electron velocities
#dlmwrite('v.txt',v,'delimiter','\t','precision','%25.15e');
