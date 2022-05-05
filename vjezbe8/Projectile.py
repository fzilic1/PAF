from re import M
from winreg import KEY_WOW64_32KEY
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self):
        self.t=[]
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]
        self.ax=[]
        self.ay=[]
        self.m=0
        self.rho=0
        self.C_d=0
        self.A=0
        self.dt=0
    
    def set_initial_conditions(self, v_0, theta, x_0, y_0, m, rho, C_d, A, t=0.001):
        
        self.m=m
        self.rho=rho
        self.C_d=C_d
        self.A=A
        
        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.vx.append(v_0*np.cos(theta*np.pi/180))
        self.vy.append(v_0*np.sin(theta*np.pi/180))
        self.dt=t

    def reset(self):
        self.__init__()

    def __move(self):
        self.ax.append(-np.sign(self.vx[-1])*self.rho*self.C_d*self.A*np.power(self.vx[-1], 2)/(2*self.m))
        self.ay.append(-9.81-np.sign(self.vy[-1])*self.rho*self.C_d*self.A*np.power(self.vy[-1], 2)/(2*self.m))
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.t.append(self.t[-1]+self.dt)
    
    def __rungekutta(self):
        self.ax.append(-np.sign(self.vx[-1])*self.rho*self.C_d*self.A*np.power(self.vx[-1], 2)/(2*self.m))
        self.ay.append(-9.81-np.sign(self.vy[-1])*self.rho*self.C_d*self.A*np.power(self.vy[-1], 2)/(2*self.m))
        
        k1v_x=self.ax[-1]*self.dt
        k1x=self.vx[-1]*self.dt
        k2v_x=(-np.sign(self.vx[-1]+k1v_x/2)*self.rho*self.C_d*self.A*np.power(self.vx[-1]+k1v_x/2, 2)/(2*self.m))*self.dt
        k2x=(self.vx[-1]+k1v_x/2)*self.dt
        k3v_x=(-np.sign(self.vx[-1]+k2v_x/2)*self.rho*self.C_d*self.A*np.power(self.vx[-1]+k2v_x/2, 2)/(2*self.m))*self.dt
        k3x=(self.vx[-1]+k2v_x/2)*self.dt
        k4v_x=(-np.sign(self.vx[-1]+k3v_x)*self.rho*self.C_d*self.A*np.power(self.vx[-1]+k3v_x, 2)/(2*self.m))*self.dt
        k4x=(self.vx[-1]+k3v_x)*self.dt

        self.vx.append(self.vx[-1]+(1/6)*(k1v_x+2*k2v_x+2*k3v_x+k4v_x))
        self.x.append(self.x[-1]+ (1/6)*(k1x+2*k2x+2*k3x+k4x))
        
        k1v_y=self.ay[-1]*self.dt
        k1y=self.vy[-1]*self.dt
        k2v_y=(-np.sign(self.vy[-1]+k1v_y/2)*self.rho*self.C_d*self.A*np.power(self.vy[-1]+k1v_y/2, 2)/(2*self.m))*self.dt
        k2y=(self.vy[-1]+k1v_y/2)*self.dt
        k3v_y=(-np.sign(self.vy[-1]+k2v_y/2)*self.rho*self.C_d*self.A*np.power(self.vy[-1]+k2v_y/2, 2)/(2*self.m))*self.dt
        k3y=(self.vy[-1]+k2v_y/2)*self.dt
        k4v_y=(-np.sign(self.vy[-1]+k3v_y)*self.rho*self.C_d*self.A*np.power(self.vy[-1]+k3v_y, 2)/(2*self.m))*self.dt
        k4y=(self.vy[-1]+k3v_y)*self.dt

        self.vy.append(self.vy[-1]+(1/6)*(k1v_y+2*k2v_y+2*k3v_y+k4v_y))
        self.y.append(self.y[-1]+ (1/6)*(k1y+2*k2y+2*k3y+k4y))
        
        
        
        self.t.append(self.t[-1]+self.dt)


    def range(self, method='E'):
        if method=='RK':
            while self.y[-1]>=0:
                self.__rungekutta()

        else:
            while self.y[-1]>=0:
                self.__move()
        
        return self.x[-1]

    def plot_trajectory(self, method='E'):
        if method=='RK':
            self.range('RK')
            plt.plot(self.x, self.y)
            plt.xlabel("x [m]")
            plt.ylabel("y [m]")
            plt.show()

        else:
            self.range()
            plt.plot(self.x, self.y)
            plt.xlabel("x [m]")
            plt.ylabel("y [m]")
            plt.show()