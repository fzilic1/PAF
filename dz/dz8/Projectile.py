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
    
    def set_initial_conditions(self, v_0, theta, x_0, y_0, m, rho, C_d, A, shape='n', t=0.001):
        
        self.m=m
        self.rho=rho
        self.C_d=C_d

        if shape=='kocka':
            self.A=np.power(A, 2)
        elif shape=='kugla':
            self.A=np.pi*np.power(A, 2)
        else:
            self.A=A

        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.vx.append(v_0*np.cos(theta*np.pi/180))
        self.vy.append(v_0*np.sin(theta*np.pi/180))
        self.dt=t

    def reset(self):
        self.__init__()

    def __acc(self, x, y, vx, vy, t ):
        a=[]
        a.append((-np.sign(vx)*self.rho*self.C_d*self.A*np.power(vx, 2))/(2*self.m))
        a.append(-9.81-(np.sign(vy)*self.rho*self.C_d*self.A*np.power(vy, 2))/(2*self.m))
        return a

    def __move(self):
        a=self.__acc(self.x[-1], self.y[-1], self.vx[-1], self.vy[-1], self.t[-1])

        self.ax.append(a[0])
        self.ay.append(a[1])
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.t.append(self.t[-1]+self.dt)
    
    def __rungekutta(self):
        a=self.__acc(self.x[-1], self.y[-1], self.vx[-1], self.vy[-1], self.t[-1])
        self.ax.append(a[0])
        self.ay.append(a[1])
        
        k1v_x=self.ax[-1]*self.dt
        k1x=self.vx[-1]*self.dt
        k1v_y=self.ay[-1]*self.dt
        k1y=self.vy[-1]*self.dt

        k2v_x=(self.__acc(self.x[-1]+k1x/2, self.y[-1]+k1y/2, self.vx[-1]+k1v_x/2, self.vy[-1]+k1v_y/2, self.t[-1]+self.dt/2)[0])*self.dt
        k2x=(self.vx[-1]+k1v_x/2)*self.dt
        k2v_y=(self.__acc(self.x[-1]+k1x/2, self.y[-1]+k1y/2, self.vx[-1]+k1v_x/2, self.vy[-1]+k1v_y/2, self.t[-1]+self.dt/2)[1])*self.dt
        k2y=(self.vy[-1]+k1v_y/2)*self.dt

        k3v_x=(self.__acc(self.x[-1]+k2x/2, self.y[-1]+k2y/2, self.vx[-1]+k2v_x/2, self.vy[-1]+k2v_y/2, self.t[-1]+self.dt/2)[0])*self.dt
        k3x=(self.vx[-1]+k2v_x/2)*self.dt
        k3v_y=(self.__acc(self.x[-1]+k2x/2, self.y[-1]+k2y/2, self.vx[-1]+k2v_x/2, self.vy[-1]+k2v_y/2, self.t[-1]+self.dt/2)[1])*self.dt
        k3y=(self.vy[-1]+k2v_y/2)*self.dt
        
        k4v_x=(self.__acc(self.x[-1]+k3x/2, self.y[-1]+k3y/2, self.vx[-1]+k3v_x/2, self.vy[-1]+k3v_y/2, self.t[-1]+self.dt/2)[0])*self.dt
        k4x=(self.vx[-1]+k3v_x)*self.dt
        k4v_y=(self.__acc(self.x[-1]+k3x/2, self.y[-1]+k3y/2, self.vx[-1]+k3v_x/2, self.vy[-1]+k3v_y/2, self.t[-1]+self.dt/2)[1])*self.dt
        k4y=(self.vy[-1]+k3v_y)*self.dt

        self.vx.append(self.vx[-1]+(1/6)*(k1v_x+2*k2v_x+2*k3v_x+k4v_x))
        self.x.append(self.x[-1]+ (1/6)*(k1x+2*k2x+2*k3x+k4x))
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

        else:
            self.range()
            plt.plot(self.x, self.y)
            plt.xlabel("x [m]")
            plt.ylabel("y [m]")

    def target(self, v_0, x_0, y_0, m, rho, C_d, A, cx, cy, r, shape='n', t=0.001):
        i=0
        theta=1
        while i==0 and theta < 90:
            self.set_initial_conditions(v_0, theta, x_0, y_0, m, rho, C_d, A, shape, t)
            while self.y[-1]>=0:
                self.__rungekutta()
                if np.sqrt(np.power(self.x[-1]-cx, 2) + np.power(self.y[-1]-cy, 2)) <= r:
                    i=1
            self.reset()
            theta+=1
        self.set_initial_conditions(v_0, theta, x_0, y_0, m, rho, C_d, A, shape, t)
        
        
        figure, axes=plt.subplots()
        self.plot_trajectory('RK')
        cc=plt.Circle((cx, cy), r)
        axes.set_aspect(1)
        axes.add_artist(cc)
        plt.show()
        return theta
