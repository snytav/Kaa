import numpy_groupies as npg
def GetDensity( r, L, J ):
# Evaluate number density n in grid of J cells, length   L, from the electron positions r

    dx = L/J

    js = floor(r/dx)+1
    ys = r/dx - (js-1)
    js_plus_1 = mod(js,J)+1
    n = npg.aggregate(js,(1-ys)/dx,[J,1]) + npg.aggregate(js_plus_1,ys/dx,[J,1])

    return n
