import numpy as np
function u = Poisson1D( v, L )
  # Solve 1-d Poisson equation:
  #     d^u / dx^2 = v   for  0 <= x <= L
  # using spectral method
  J = len(v)
  # Fourier transform source term
  v_tilde = np.fft(v);
  # vector of wave numbers
  k = (2*pi/L)*[0:(J/2-1) (-J/2):(-1)]
  k[0] = 1
  # Calculate Fourier transform of u
  u_tilde = -v_tilde./k.^2
  # Inverse Fourier transform to obtain u
  u = real(np.ifft(u_tilde))
  # Specify arbitrary constant by forcing corner u = 0;
  u = u - u(1)
end 
