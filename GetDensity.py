import numpy_groupies as npg
import numpy as np
def GetDensity( r, L, J ):
# Evaluate number density n in grid of J cells, length   L, from the electron positions r

    dx = L/J

    js = np.floor(r/dx)
    ys = r/dx - (js)
    js_plus_1 = np.mod(js,J)+1
    n1 = npg.aggregate(js,(1-ys)/dx,[J,1])
    n2 = npg.aggregate(js_plus_1,ys/dx,[J,1])

    n = n1 + n2

    return n
