import numpy as np
import matplotlib.pyplot as plt
import Object as o

class Inter:
    def __init__(self):
        self.G=6.67408*np.power(10, -11)
        self.dt=0
        self.p=0
        self.planets=[]

    def initial(self, p, dt=0.1):
        self.p=p
        self.dt=dt*86400

    def reset(self):
        self.__init__()

    def addplanet(self, o.planet):
        self.planets.append(o.planet)

    def __move(self):
        for p in self.planets:
            for i in self.planets:
                if i != p:
                    self.planets[p].a=-self.G*self.planets[i].m*(self.planets[p].r-self.planets[i].r)/np.power(np.absolute(self.planets[p].r-self.planets[i].r), 3)
                    self.planets[p].v+=self.planets[p].a*self.dt
                    self.planets[p].r+=self.planets[p].v*self.dt

                    self.planets[i].a=-self.G*self.planets[p].m*(self.planets[i].r-self.planets[p].r)/np.power(np.absolute(self.planets[i].r-self.planets[p].r), 3)
                    self.planets[i].v+=self.planets[i].a*self.dt
                    self.planets[i].r+=self.planets[i].v*self.dt

                    self.planets[p].x.append(self.planets[p].r[0])
                    self.planets[p].y.append(self.planets[p].r[1])
                    self.planets[p].t.append(self.planets[p].t[-1]+self.dt)

                    self.planets[i].x.append(self.planets[i].r[0])
                    self.planets[i].y.append(self.planets[i].r[1])
                    self.planets[i].t.append(self.planets[i].t[-1]+self.dt)

    def inter(self, T):
        while self.planets[self.p].t[-1] < T:
            self.__move()
            plt.plot(self.planets[1].x, self.planets[1].y)
            plt.show()