import matplotlib.pyplot as plt
import numpy as np

def putanja(v0, theta):
    dt=0.05
    g=-9.81
    x=[0]
    y=[0]
    xi=0
    yi=0

    thetarad=theta*np.pi/180
    vix=v0*np.cos(thetarad)
    viy=v0*np.sin(thetarad)

    while True:
        xi+=vix*dt
        yi+=viy*dt
        viy+=g*dt
        if yi>0:
            x.append(xi)
            y.append(yi)
        else:
            break;

    fig, axs =plt.subplots(1)
    axs.plot(x, y, '-r')
    axs.set(xlabel='x [m]', ylabel='y [m]')

    plt.show()


def maxh(v0, theta):
    dt=0.05
    g=-9.81
    x=[0]
    y=[0]
    xi=0
    yi=0
    hmax=0

    thetarad=theta*np.pi/180
    vix=v0*np.cos(thetarad)
    viy=v0*np.sin(thetarad)

    while True:
        xi+=vix*dt
        yi+=viy*dt
        viy+=g*dt
        if yi>hmax:
            hmax=yi
        if yi>0:
            x.append(xi)
            y.append(yi)
        else:
            break;
        
    return hmax

def domet(v0, theta):
    dt=0.05
    g=-9.81
    x=[0]
    y=[0]
    xi=0
    yi=0

    thetarad=theta*np.pi/180
    vix=v0*np.cos(thetarad)
    viy=v0*np.sin(thetarad)

    while True:
        xi+=vix*dt
        yi+=viy*dt
        viy+=g*dt
        if yi>0:
            x.append(xi)
            y.append(yi)
        else:
            break;
        
    return xi

def maxv(v0, theta):
    dt=0.05
    g=-9.81
    x=[0]
    y=[0]
    xi=0
    yi=0
    vymax=0

    thetarad=theta*np.pi/180
    vix=v0*np.cos(thetarad)
    viy=v0*np.sin(thetarad)

    while True:
        xi+=vix*dt
        yi+=viy*dt
        if abs(viy)>vymax:
            vymax=abs(viy)
        viy+=g*dt
        if yi>0:
            x.append(xi)
            y.append(yi)
        else:
            break;
    
    vmax=np.sqrt(vix**2+vymax**2)
    return vmax

def meta(v0, theta, Cx, Cy, r):
    dt=0.05
    g=-9.81
    x=[0]
    y=[0]
    xi=0
    yi=0

    thetarad=theta*np.pi/180
    vix=v0*np.cos(thetarad)
    viy=v0*np.sin(thetarad)

    while True:
        xi+=vix*dt
        yi+=viy*dt
        viy+=g*dt
        if yi>0:
            x.append(xi)
            y.append(yi)
        else:
            break;

    k=0
    Dmin=np.sqrt((Cx-x[0])**2+(Cy-y[0])**2)
    for i in range(len(x)):
        D=np.sqrt((Cx-x[i])**2+(Cy-y[i])**2)
        if D<=r and k==0:
            print ("Meta je pogođena")
            k=1
        else:
            if D<Dmin:
                Dmin=D
    if k==0:
        dis=Dmin-r
        print ("Udaljenost od mete je "+str(dis))

    fig, axs =plt.subplots(1)
    axs.plot(x, y, '-r')
    axs.set(xlabel='x [m]', ylabel='y [m]')
    plt.axis("equal")
    c=plt.Circle((Cx, Cy), radius=r)
    plt.gca().add_artist(c)

    plt.show()