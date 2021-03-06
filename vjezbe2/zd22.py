import matplotlib.pyplot as plt
import numpy as np

def kosi_hitac(v0, theta):
    vrijeme=10
    dt=0.05
    g=-9.81
    t=[]
    x=[]
    y=[]
    xi=0
    yi=0

    thetarad=theta*np.pi/180
    vix=v0*np.cos(thetarad)
    viy=v0*np.sin(thetarad)

    for i in range(int(vrijeme/dt)):
        t.append(i*dt)
        xi+=vix*dt
        x.append(xi)
        yi+=viy*dt
        viy+=g*dt
        y.append(yi)

    fig, axs =plt.subplots(1, 3)
    axs[0].plot(x, y, '-r')
    axs[1].plot(t, x, '-g')
    axs[2].plot(t, y, '-b')
    
    axs[0].set(xlabel='x [m]', ylabel='y [m]')
    axs[1].set(xlabel='t [s]', ylabel='x [m]')
    axs[2].set(xlabel='t [s]', ylabel='y [m]')
    plt.show()