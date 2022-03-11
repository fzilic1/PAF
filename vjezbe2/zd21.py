import matplotlib.pyplot as plt

def sila(F, m):
    a=F/m

    vrijeme=10
    dt=0.05
    t=[]
    acc=[]
    v=[]
    s=[]
    vi=0
    si=0

    for i in range(int(vrijeme/dt)):
        t.append(i*dt)
        acc.append(a)
        vi+=a*dt
        v.append(vi)
        si+=vi*dt
        s.append(si)

    fig, axs =plt.subplots(3)
    axs[0].plot(t, acc, '-g')
    axs[1].plot(t, v, '-b')
    axs[2].plot(t, s, '-r')
    
    for ax in axs.flat:
        ax.set(xlabel='t [s]')
        ax.label_outer()
    axs[0].set(ylabel='a [m/$s^2$]')
    axs[1].set(ylabel='v [m/s]')
    axs[2].set(ylabel='s [m]')
    plt.show()

sila(5, 7)