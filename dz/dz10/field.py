import numpy as np

def __a(q, E, B, v, m):
    F=q*E+q*np.cross(v, B)
    a=F/m
    return a

def mov(q, m, v, B, E, T, method='E', dt=0.001):
    x=[0]
    y=[0]
    z=[0]
    t=[0]
    a=np.array([0,0,0])
    
    if method == 'RK':
        while t[-1] < T:
            a=__a(q, E(t[-1]), B(t[-1]), v, m)

            k1v=a*dt
            k1=v*dt

            a=__a(q, E(t[-1]), B(t[-1]), v+(k1v/2), m)
            k2v=a*dt
            k2=(v+(k1v/2))*dt

            a=__a(q, E(t[-1]), B(t[-1]), v+(k2v/2), m)
            k3v=a*dt
            k3=(v+(k2v/2))*dt

            a=__a(q, E(t[-1]), B(t[-1]), v+(k3v/2), m)
            k4v=a*dt
            k4=(v+(k3v/2))*dt

            v=v+(1/6)*(k1v+2*k2v+2*k3v+k4v)
            x.append(x[-1]+(1/6)*(k1[0]+2*k2[0]+2*k3[0]+k4[0]))
            y.append(y[-1]+(1/6)*(k1[1]+2*k2[1]+2*k3[1]+k4[1]))
            z.append(z[-1]+(1/6)*(k1[2]+2*k2[2]+2*k3[2]+k4[2]))

            t.append(t[-1]+dt)

    else:    
        while t[-1] < T:
            a=__a(q, E(t[-1]), B(t[-1]), v, m)
            v=v+a*dt

            x.append(x[-1]+v[0]*dt)
            y.append(y[-1]+v[1]*dt)
            z.append(z[-1]+v[2]*dt)
            t.append(t[-1]+dt)

    return ((x, y, z))