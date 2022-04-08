def pos(x_0, v_0, m, t, dt):
    T=0
    x=x_0
    v=v_0
    while T <= t:
        F=T**2+2*v+x
        a=F/m
        x+=v*dt
        v+=a*dt
        T+=dt
    return x

def vel(x_0, v_0, m, t, dt):
    T=0
    x=x_0
    v=v_0
    while T <= t:
        F=T**2+2*v+x
        a=F/m
        x+=v*dt
        v+=a*dt
        T+=dt
    return v

def acc(x_0, v_0, m, t, dt):
    T=0
    x=x_0
    v=v_0
    while T <= t:
        F=T**2+2*v+x
        a=F/m
        x+=v*dt
        v+=a*dt
        T+=dt
    return a