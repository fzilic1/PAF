def dev(f, x, h=0.01, method='3'):
    if method=='2':
        return ((f(x+h)-f(x))/h)
    else:
        return ((f(x+h)-f(x-h))/(2*h))

def devrange(f, a, b, h=0.01, method='3'):
    t=[]
    dt=[]
    i=a

    while i <= b:
        t.append(i)
        dt.append(dev(f, i, h, method))
        i+=h

    return [t, dt]

def intlim(f, a, b, N):
    dx=(b-a)/N
    
    i=a
    F_l=0
    while i < b:
        F_l+=f(i)*dx
        i+=dx
        i=round(i, 7)
    
    i=a+dx
    F_u=0
    while i <= b:
        F_u+=f(i)*dx
        i+=dx
        i=round(i, 7)

    return F_l, F_u

def numint(f, a, b, N):
    dx=(b-a)/N
    i=a
    F=dx*0.5*(f(a)+f(b))
    while i <= b:
        F+=dx*f(i)
        i+=dx
    return F