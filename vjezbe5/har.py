import matplotlib.pyplot as plt
import harmonic_oscilator as har

h=har.HarmonicOscilator()
h.initial(2, 8, 2, 0, 0, 0.01)
h.oscilate(12.56)
fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].plot(h.t, h.x)
axs[1].plot(h.t, h.vx)
axs[2].plot(h.t, h.ax)
plt.show()