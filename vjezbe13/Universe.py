import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import Planet as pl
from matplotlib.animation import FuncAnimation

class Universe:
    def __init__(self):
        self.G=6.67408*np.power(10.0, -11)
        self.dt=0
        self.p=0
        self.planets=[]

    def initial(self, p, dt=0.1):
        self.p=p-1
        self.dt=dt*86400

    def reset(self):
        self.__init__()

    def addplanet(self, planet):
        self.planets.append(planet)

    def __move(self):
        for p in range(len(self.planets)):
            self.planets[p].a=np.array([0.0, 0.0])
            for i in range(len(self.planets)):
                if i != p:
                    self.planets[p].a+= -self.G*self.planets[i].m*(self.planets[p].r-self.planets[i].r)/np.power(LA.norm(self.planets[p].r-self.planets[i].r), 3)
                    
            self.planets[p].v=self.planets[p].v+self.planets[p].a*self.dt
            self.planets[p].r=self.planets[p].r+self.planets[p].v*self.dt

            self.planets[p].x.append(self.planets[p].r[0])
            self.planets[p].y.append(self.planets[p].r[1])
            self.planets[p].t.append(self.planets[p].t[-1]+self.dt)

    def evolve(self, T):
        while self.planets[self.p].t[-1] < T:
            self.__move()
        
        fig, axs=plt.subplots(1)
        for i in range(self.p+1):
            axs.plot(self.planets[i].x, self.planets[i].y, color=self.planets[i].color)
            circle=plt.Circle((self.planets[i].x[-1], self.planets[i].y[-1]), 0.5*np.power(10.0, 10), color=self.planets[i].color)
            axs.add_patch(circle)
        
        axs.set_aspect(1)
        plt.show()

    def animate(self, T, frame):
        while self.planets[self.p].t[-1] < T:
            self.__move()

        fig, ax=plt.subplots()
        ax.set_xlim([-1.7*np.power(10.0, 11), 3.35*np.power(10.0, 11)])
        ax.set_ylim([-2.32*np.power(10.0, 11), 3.25*np.power(10.0, 11)])
        ax.set_aspect(1)
        def anima1(i):
            ax.clear()
            ax.set_xlim([-1.7*np.power(10.0, 11), 3.35*np.power(10.0, 11)])
            ax.set_ylim([-2.32*np.power(10.0, 11), 3.25*np.power(10.0, 11)])
            ax.set_aspect(1)
            for j in range(len(self.planets)):
                ax.scatter(x=self.planets[j].x[i], y=self.planets[j].y[i], c=self.planets[j].color, lw=1)

        def anima2(i):
            for j in range(len(self.planets)):
                ax.plot(self.planets[j].x[:i], self.planets[j].y[:i], color=self.planets[j].color)

        anim1=FuncAnimation(fig, func=anima1, frames=frame, interval=20)
        anim2=FuncAnimation(fig, func=anima2, frames=frame, interval=20)
        plt.show()

    def hit(self, T, frame):
        theta=1
        a=0
        v0=[]
        for i in range(len(self.planets)):
            v0.append(self.planets[i].v)
        while theta<90 and a==0:
            for i in range(len(self.planets)):
                xq=self.planets[i].x[0]
                yq=self.planets[i].y[0]
                self.planets[i].x=[xq]
                self.planets[i].y=[yq]
                self.planets[i].r=np.array([self.planets[i].x[0], self.planets[i].y[0]])
                self.planets[i].v=v0[i]
                self.planets[i].a=np.array([0.0, 0.0])

            self.planets[5].v=np.array([-15000.0*np.cos(theta*np.pi/180.0), -15000.0*np.sin(theta*np.pi/180.0)])

            while self.planets[self.p].t[-1] < T:
                self.__move()
                d=np.sqrt(np.power((self.planets[5].x[-1]-self.planets[2].x[-1]), 2) + np.power((self.planets[5].y[-1]-self.planets[2].y[-1]), 2))
                if a==1:
                    self.planets[5].x[-1]=self.planets[5].x[-2]
                    self.planets[5].y[-1]=self.planets[5].y[-2]
                if d <= np.power(10.0, 11):
                    a=1
            theta+=1

        fig, axs=plt.subplots(1)
        for i in range(self.p+1):
            axs.plot(self.planets[i].x, self.planets[i].y, color=self.planets[i].color)
            circle=plt.Circle((self.planets[i].x[-1], self.planets[i].y[-1]), 0.5*np.power(10.0, 10), color=self.planets[i].color)
            axs.add_patch(circle)
        
        axs.set_aspect(1)
        plt.show()