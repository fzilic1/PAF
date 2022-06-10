import numpy as np

class Planet:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.r=np.array([0, 0])
        self.v=np.array([0, 0])
        self.a=np.array([0, 0])
        self.t=[]
        self.m=0
        self.color='color'

    def initial(self, x0, y0, v0, m, color='blue'):
        self.t.append(0.0)
        self.x.append(x0)
        self.y.append(y0)
        self.r=np.array([x0, y0])
        self.v=np.array([v0, 0.0])
        self.a=np.array([0.0, 0.0])
        self.m=m
        self.color=color

    def reset(self):
        self.__init__()