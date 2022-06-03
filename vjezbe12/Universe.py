import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import Planet as pl

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
            axs.plot(self.planets[i].x, self.planets[i].y)
            circle=plt.Circle((self.planets[i].x[-1], self.planets[i].y[-1]), 0.5*np.power(10.0, 10))
            axs.add_patch(circle)
        
        axs.set_aspect(1)
        plt.show()