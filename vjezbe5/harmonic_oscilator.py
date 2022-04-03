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

    def initial(self, k, m, x_0, v_0, dt):
        self.t.append(0)
        self.x.append(x_0)
        self.vx.append(v_0)
        self.ax.append(-(k/m)*x_0)
        self.dt=dt
        self.k=k
        self.m=m

    def reset(self):
        self.__init__()

    def __move(self):
        self.ax.append(-(self.k/self.m)*self.x[-1])
        self.t.append(self.t[-1]+self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)

    def period(self, k, m, x_0, v_0, dt):
        self.initial(k, m, x_0, v_0, dt)
        T=0
        self.__move()
        if self.x[-1] >=0:
            while abs(self.x[-1]) == self.x[-1]:
                self.__move()
            while abs(self.x[-1]) != self.x[-1]:
                self.__move()
                T+=dt
        elif self.x[-1] < 0:
            while abs(self.x[-1]) != self.x[-1]:
                self.__move()
            while abs(self.x[-1]) == self.x[-1]:
                self.__move()
                T+=dt
        return(2*T)

    def oscilate(self, R):
        while self.t[-1] <= R:
            self.__move()