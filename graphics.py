import matplotlib.pyplot as plt

def phase_space(t,dt,r,v):
    plt.scatter(r,v,s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    tit = 'Electron Phase-space distribution for t = ' + str(t)
    plt.title(tit)