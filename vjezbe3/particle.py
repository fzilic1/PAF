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

    def total_time(self):
        self.range()
        return self.t[-1]

    def max_speed(self):
        vmax=0
        self.range()
        for i in range(len(self.vx)):
            V=np.sqrt(self.vx[i]**2+self.vy[i]**2)
            if V>vmax:
                vmax=V
        return vmax

    def velocity_to_hit_target(self, theta, Cx, Cy, r, t):
        v0=0
        V=0
        while V==0:
            self.set_initial_conditions(v0, theta, 0, 0, t)
            self.range()
            for i in range(len(self.x)):
                DI=np.sqrt((Cx-self.x[i])**2+(Cy-self.y[i])**2)
                if DI<=r:
                    V=v0
                    break;
            self.reset()
            v0+=0.1
        return V

    def angle_to_hit_target(self, v0, Cx, Cy, r, t):
        theta=0
        THETA=0
        while THETA==0:
            self.set_initial_conditions(v0, theta, 0, 0, t)
            self.range()
            for i in range(len(self.x)):
                DI=np.sqrt((Cx-self.x[i])**2+(Cy-self.y[i])**2)
                if DI<=r:
                    THETA=theta
                    break;
            self.reset()
            theta+=1
        return THETA