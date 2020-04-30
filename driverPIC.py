am velocity
dt = 0.1   # time-step (in inverse plasma frequencies)
tmax = 80  # simulafrom numpy import random
import numpy as np
import double_maxwellian

L = 100    # domain of solution 0 <= x <= L
N = 20000  # number of electrons
J = 1000   # number of grid points
vb = 3     # betion run from t = 0 to t = tmax

#initialize solution
t = 0
np.rng(42)                              # seed the rand generator
r = L*random.uniform(0,1,N)             # electron positions
#dlmwrite('r.txt',r,'delimiter','\t','precision','%25.15e');
v = double_maxwellian(N,vb)             # electron velocities
#dlmwrite('v.txt',v,'delimiter','\t','precision','%25.15e');

#evolve solution
while t<=tmax:
    # load r,v into a single vector
    solution_coeffs = np.concatenate(r,v)
    
    # take a 4th order Runge-Kutta timestep
    k1 = AssembleRHS(solution_coeffs,L,J,N)
    k2 = AssembleRHS(solution_coeffs + 0.5*dt*k1,L,J,N)
    k3 = AssembleRHS(solution_coeffs + 0.5*dt*k2,L,J,N)
    k4 = AssembleRHS(solution_coeffs + dt*k3,L,J,N)
    solution_coeffs = solution_coeffs + dt/6*(k1+2*k2+2*k3+k4)
    # unload solution coefficients
    r = solution_coeffs[0:N-1]
    v = solution_coeffs[N:2*N - 1]
    # make sure all coordinates are in the range 0 to L
    r = r + L*(r<0) - L*(r>L)
    t = t + dt
    
    detailed_output(t,dt,solution_coeffs,k1,k2,k3,k4);
    phase_space(t,dt,r,v);
   
end
