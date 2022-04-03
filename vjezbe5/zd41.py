import matplotlib.pyplot as plt
import harmonic_oscilator as har
import numpy as np

h=har.HarmonicOscilator()
k=har.HarmonicOscilator()
j=har.HarmonicOscilator()

p=h.period(4, 3, 6, 0, 0.1)
k.initial(4, 3, 6, 0, 0.05)
j.initial(4, 3, 6, 0, 0.01)

h.oscilate(p)
k.oscilate(p)
j.oscilate(p)

Xa=[]
for i in range(len(h.t)):
    Xa.append(6*np.sin(h.t[i]*np.sqrt(4/3)+np.pi/2))

plt.plot(h.t, Xa)
plt.plot(h.t, h.x, linestyle='dotted')
plt.plot(k.t, k.x, linestyle='-.')
plt.plot(j.t, j.x, linestyle='dashed')

plt.legend(["analitički", "dt=0.1", "dt=0.05", "dt=0.01"])
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.show()