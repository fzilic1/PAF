import matplotlib.pyplot as plt

class ProjectileDrop:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.vx=[]
        self.vy=[]
        self.ax=[]
        self.ay=[]
        self.t=[]

    def set_init(self, h, vx):
        self.t.append(0)
        self.y.append(h)
        self.x.append(0)
        self.vx.append(vx)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.dt=0.01
        print ("Stvoren je projektil na visini "+str(h)+" m s početnom brzinom "+str(vx)+" m/s")

    def reset(self):
        self.__init__()

    def new_h(self, h):
        self.y[0]=h

    def new_vx(self, vx):
        self.vx[0]+=vx

    def drop(self):
        while self.y[-1] > 0:
            self.t.append(self.t[-1]+self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
            self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
            self.ax.append(0)
            self.ay.append(-9.81)

    def drop_time(self, dt):
        self.dt=dt
        while self.y[-1] > 0:
            self.t.append(self.t[-1]+self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
            self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
            self.ax.append(0)
            self.ay.append(-9.81)
        return (self.t[-1])

    def target(self, h, vx, x, d, v):
        i=1
        t=0
        while i==1:
            self.set_init(h, vx)
            self.x[0]=vx*t
            self.vx[0]+=v
            self.drop()
            if self.x[-1] < (x+d) and self.x[-1] > (x-d):
                i=0
                plt.plot(self.x, self.y)
                plt.xlabel('x [m]')
                plt.ylabel('y [m]')
                plt.show()
                return t
            else:
                self.reset()
                t+=0.1
