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

    def animate(self, T):
        while self.planets[self.p].t[-1] < T:
            self.__move()

        fig = plt.figure()
        ax = plt.axes(xlim=(-2.5*np.power(10.0, 11), 2.5*np.power(10.0, 11)), ylim=(-2.5*np.power(10.0, 11), 2.5*np.power(10.0, 11)))
        ax.set_aspect(1)
        line, = ax.plot([], [], lw=2)
        
        plotlays, plotcols = [6], ["yellow","blue", "red", "violet", "orange", "brown"]
        lines=[]
        for index in range(6):
            lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
            lines.append(lobj)

        def init():
            for line in lines:
                line.set_data([],[])
            return lines

        x1data, y1data = [], []
        x2data, y2data = [], []
        x3data, y3data = [], []
        x4data, y4data = [], []
        x5data, y5data = [], []
        x6data, y6data = [], []

        def anima(i):
            x=self.planets[0].x[i]
            y=self.planets[0].y[i]
            x1data.append(x)
            y1data.append(y)

            x=self.planets[1].x[i]
            y=self.planets[1].y[i]
            x2data.append(x)
            y2data.append(y)

            x=self.planets[2].x[i]
            y=self.planets[2].y[i]
            x3data.append(x)
            y3data.append(y)

            x=self.planets[3].x[i]
            y=self.planets[3].y[i]
            x4data.append(x)
            y4data.append(y)
            
            x=self.planets[4].x[i]
            y=self.planets[4].y[i]
            x5data.append(x)
            y5data.append(y)

            x=self.planets[5].x[i]
            y=self.planets[5].y[i]
            x6data.append(x)
            y6data.append(y)

            xlist=[x1data, x2data, x3data, x4data, x5data, x6data]
            ylist=[y1data, y2data, y3data, y4data, y5data, x6data]
            for lnum,line in enumerate(lines):
                line.set_data(xlist[lnum], ylist[lnum])

            return lines

        anim=FuncAnimation(fig, anima, init_func=init, frames=4000, interval=20, blit='True')
        plt.show()