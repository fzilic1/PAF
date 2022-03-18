import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.t=[]
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]
        self.ax=[]
        self.ay=[]
        self.dt=0
    
    def set_initial_conditions(self, v_0, theta, x_0, y_0, t):
        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.vx.append(v_0*np.cos(theta*np.pi/180))
        self.vy.append(v_0*np.sin(theta*np.pi/180))
        self.ax.append(0)
        self.ay.append(-9.81)
        self.dt=t

    def reset(self):
        self.__init__()

    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.ax.append(0)
        self.ay.append(-9.81)


    def range(self):
        while self.y[-1]>=0:
            self.__move()
        
        return self.x[-1]

    def plot_trajectory(self):
        self.range()
        plt.plot(self.x, self.y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()

