import particle as prt
import numpy as np
import matplotlib.pyplot as plt

v0=10
alpha=60
dt=[0]
Err=[0]

p=prt.Particle()

for i in range(10):
    p.set_initial_conditions(v0, alpha, 0, 0, dt[i])
    D_ana=((v0**2)*np.sin(2*alpha*np.pi/180)/9.81)
    D_num=p.range()
    dt.append(dt[-1]+0.01)
    Err.append[100*abs(D_ana-D_num)/D_ana]
    p.reset()

plt.plot(dt, Err)
plt.xlabel("dt [s]")
plt.ylabel("Relativna pogreška [%]")
plt.show()