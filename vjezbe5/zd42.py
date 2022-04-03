import harmonic_oscilator as har
import matplotlib.pyplot as plt
import numpy as np

h=har.HarmonicOscilator()

dt=0.5
ana=2*np.pi*np.sqrt(4/7)
DT=[]
T=[]
A=[]
for i in range(50):
    p=h.period(7, 4, 9, 0, dt)
    DT.append(dt)
    T.append(p)
    A.append(ana)
    h.reset()
    dt-=0.01

plt.plot(DT, A)
plt.plot(DT, T, 'ro')
plt.xlabel("dt [s]")
plt.ylabel("T [s]")
plt.legend(["analitički", "numerički"])
plt.show()