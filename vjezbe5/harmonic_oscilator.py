import math
import matplotlib.pyplot as plt

class HarmonicOscilator:
    def __init__(self):
        self.k=0
        self.m=0
        self.t=[]
        self.x=[]
        self.vx=[]
        self.ax=[]
        self.dt=0

    def initial(self, k, m, x_0, v_0, a_0, dt):
        self.t.append(0)
        self.x.append(x_0)
        self.vx.append(v_0)
        self.ax.append(a_0)
        self.dt=dt
        self.k=k
        self.m=m

    def reset(self):
        self.__init__()

    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.ax.append(self.ax[-1]-(self.k/self.m)*self.x[-1])
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)

    def plot_xt(self):
        max=0
        i=0
        while i==0:
            self.__move()
            if self.x[-1] > max:
                max=self.x[-1]
            elif self.x[-1]==max:
                plt.plot(self.t, self.x)
                i=1
        plt.show()