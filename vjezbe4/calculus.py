def dev(f, x, h, method):
    if method=='two-point':
        return ((f(x+h)-f(x))/h)
    else:
        return ((f(x+h)-f(x-h))/(2*h))

def devrange(f, a, b, N, h, method):
    t=[]
    dt=[]
    i=a
    step=(b-a)/N

    while i <=b:
        t.append(i)
        dt.append(dev(f, i, h, method))
        i+=step

    return [t, dt]
    
