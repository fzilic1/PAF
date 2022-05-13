import numpy as np
import matplotlib.pyplot as plt


def acc(y, v, C_d, A, rho, m, k, l_0, h_0):
    ac=-9.81-(np.sign(v)*rho*C_d*A*np.power(v, 2))/(2*m)-(k/m)*(l_0-(h_0-y))
    return ac

def bungee(h_0, m, k, l_0, C_d, A, rho, T, dt=0.001):
    y=[h_0]
    v=[0]
    a=[0]
    t=[0]

    while t[-1] < T:
        if (h_0-y[-1]) <= l_0:
            a.append(acc(y[-1], v[-1], C_d, A, rho, m, 0, l_0, h_0))
            
            k1v_y=a[-1]*dt
            k1y=v[-1]*dt

            k2v_y=acc(y[-1]+k1y/2, v[-1]+k1v_y/2, C_d, A, rho, m, 0, l_0, h_0)*dt
            k2y=(v[-1]+k1v_y/2)*dt

            k3v_y=acc(y[-1]+k2y/2, v[-1]+k2v_y/2, C_d, A, rho, m, 0, l_0, h_0)*dt
            k3y=(v[-1]+k2v_y/2)*dt

            k4v_y=acc(y[-1]+k3y/2, v[-1]+k3v_y/2, C_d, A, rho, m, 0, l_0, h_0)*dt
            k4y=(v[-1]+k3v_y)*dt

            v.append(v[-1]+(1/6)*(k1v_y+2*k2v_y+2*k3v_y+k4v_y))
            y.append(y[-1]+ (1/6)*(k1y+2*k2y+2*k3y+k4y))

            t.append(t[-1]+dt)
        else:
            a.append(acc(y[-1], v[-1], C_d, A, rho, m, k, l_0, h_0))
            
            k1v_y=a[-1]*dt
            k1y=v[-1]*dt

            k2v_y=acc(y[-1]+k1y/2, v[-1]+k1v_y/2, C_d, A, rho, m, k, l_0, h_0)*dt
            k2y=(v[-1]+k1v_y/2)*dt

            k3v_y=acc(y[-1]+k2y/2, v[-1]+k2v_y/2, C_d, A, rho, m, k, l_0, h_0)*dt
            k3y=(v[-1]+k2v_y/2)*dt

            k4v_y=acc(y[-1]+k3y/2, v[-1]+k3v_y/2, C_d, A, rho, m, k, l_0, h_0)*dt
            k4y=(v[-1]+k3v_y)*dt

            v.append(v[-1]+(1/6)*(k1v_y+2*k2v_y+2*k3v_y+k4v_y))
            y.append(y[-1]+ (1/6)*(k1y+2*k2y+2*k3y+k4y))

            t.append(t[-1]+dt)

    plt.plot(t, y)
    plt.ylabel('y [m]')
    plt.xlabel('t [s]')


def energy(h_0, m, k, l_0, C_d, A, rho, T, dt=0.001):
    y=[h_0]
    v=[0]
    a=[0]
    t=[0]

    while t[-1] < T:
        if (h_0-y[-1]) <= l_0:
            a.append(acc(y[-1], v[-1], C_d, A, rho, m, 0, l_0, h_0))
            
            k1v_y=a[-1]*dt
            k1y=v[-1]*dt

            k2v_y=acc(y[-1]+k1y/2, v[-1]+k1v_y/2, C_d, A, rho, m, 0, l_0, h_0)*dt
            k2y=(v[-1]+k1v_y/2)*dt

            k3v_y=acc(y[-1]+k2y/2, v[-1]+k2v_y/2, C_d, A, rho, m, 0, l_0, h_0)*dt
            k3y=(v[-1]+k2v_y/2)*dt

            k4v_y=acc(y[-1]+k3y/2, v[-1]+k3v_y/2, C_d, A, rho, m, 0, l_0, h_0)*dt
            k4y=(v[-1]+k3v_y)*dt

            v.append(v[-1]+(1/6)*(k1v_y+2*k2v_y+2*k3v_y+k4v_y))
            y.append(y[-1]+ (1/6)*(k1y+2*k2y+2*k3y+k4y))

            t.append(t[-1]+dt)
        else:
            a.append(acc(y[-1], v[-1], C_d, A, rho, m, k, l_0, h_0))
            
            k1v_y=a[-1]*dt
            k1y=v[-1]*dt

            k2v_y=acc(y[-1]+k1y/2, v[-1]+k1v_y/2, C_d, A, rho, m, k, l_0, h_0)*dt
            k2y=(v[-1]+k1v_y/2)*dt

            k3v_y=acc(y[-1]+k2y/2, v[-1]+k2v_y/2, C_d, A, rho, m, k, l_0, h_0)*dt
            k3y=(v[-1]+k2v_y/2)*dt

            k4v_y=acc(y[-1]+k3y/2, v[-1]+k3v_y/2, C_d, A, rho, m, k, l_0, h_0)*dt
            k4y=(v[-1]+k3v_y)*dt

            v.append(v[-1]+(1/6)*(k1v_y+2*k2v_y+2*k3v_y+k4v_y))
            y.append(y[-1]+ (1/6)*(k1y+2*k2y+2*k3y+k4y))

            t.append(t[-1]+dt)

    E_gp=[]
    E_ep=[]
    E_k=[]
    E=[]
    for i in range(len(y)):
        E_gp.append(m*9.81*y[i])
        E_ep.append(0.5*k*np.power(l_0-(h_0-y[i]),2))
        E_k.append(0.5*m*np.power(v[i],2))
        E.append(E_gp[-1]+E_ep[-1]+E_k[-1])

    plt.plot(t, E_gp)
    plt.plot(t, E_ep)
    plt.plot(t, E_k)
    plt.plot(t, E)
    plt.legend(['E_gp', 'E_ep', 'E_k', 'E'])
    plt.ylabel('E [J]')
    plt.xlabel('t [s]')

