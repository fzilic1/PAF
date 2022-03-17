import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v_0, theta, x_0, y_0):
        self.v_0=v_0
        self.theta=theta
        self.x_0=x_0
        self.y_0=y_0
    
    def set_initial_conditions(self, v_0, theta, x_0, y_0):
        self.v_0=v_0
        self.theta=theta
        self.x_0=x_0
        self.y_0=y_0

    def reset(self):
        self.v_0=0
        self.theta=0
        self.x_0=0
        self.y_0=0

    def __move(self):
        dt=0.05
        self.x_0+=v_0*np.cos(self.theta*180/np.pi())*dt
        self.y_0+=v_0*np.sin(self.theta*180/np.pi())*dt

    def range(self):
        while self.y_0>0:
            __move(self)
        
        return self.x_0

    def plot_trajectory(self):
        x=[]
        y=[]
        while self.y_0>0:
            x.append(self.x_0)
            y.append(self.y_0)
            __move(self)
        
        plt.plot(x, y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()

