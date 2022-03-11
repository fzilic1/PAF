import matplotlib.pyplot as plt
import numpy as np

def kosi_hitac(v0, theta):
    vrijeme=10
    dt=1
    g=-9.81
    t=[]
    x=[]
    y=[]
    xi=0
    yi=0

    theta=360*theta/(2*np.pi)
    vix=v0*np.cos(theta)
    viy=v0*np.sin(theta)

    for i in range(int(vrijeme/dt)):
        t.append(i)
        xi+=vix*dt
        x.append(xi)
        viy+=g*dt
        yi+=viy*dt
        y.append(yi)

    fig, axs =plt.subplots(2)
    axs[0].plot(t, x, '-g')
    axs[1].plot(t, y, '-b')
    
    for ax in axs.flat:
        ax.set(xlabel='t [s]')
        ax.label_outer()
    axs[0].set(ylabel='x [m]')
    axs[1].set(ylabel='y [m]')
    plt.show()

kosi_hitac(5, 30)