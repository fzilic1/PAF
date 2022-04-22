from turtle import pd
import ProjectileDrop as pd
import matplotlib.pyplot as plt

p=pd.ProjectileDrop()
p.set_init(2000, 200)

DT=[]
T=[]
t=0.001
for i in range(100):
    DT.append(t)
    T.append(p.drop_time(t))
    t+=0.001
    p.reset()
    p.set_init(2000, 200)

plt.plot(DT, T)
plt.xlabel('dt [s]')
plt.ylabel('T [s]')
plt.show()