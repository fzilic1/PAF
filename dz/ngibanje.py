def pos(x_0, v_0, m, t, dt, n1, n2, n3, n4):
    T=0
    x=x_0
    v=v_0
    while T <= t:
        F=n1*v+n2*x+n3*t+n4
        a=F/m
        x+=v*dt
        v+=a*dt
        T+=dt
    return x

def vel(x_0, v_0, m, t, dt, n1, n2, n3, n4):
    T=0
    x=x_0
    v=v_0
    while T <= t:
        F=n1*v+n2*x+n3*t+n4
        a=F/m
        x+=v*dt
        v+=a*dt
        T+=dt
    return v

def acc(x_0, v_0, m, t, dt, n1, n2, n3, n4):
    T=0
    x=x_0
    v=v_0
    while T <= t:
        F=n1*v+n2*x+n3*t+n4
        a=F/m
        x+=v*dt
        v+=a*dt
        T+=dt
    return a