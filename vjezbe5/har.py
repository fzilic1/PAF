import matplotlib.pyplot as plt
import harmonic_oscilator as har

h=har.HarmonicOscilator()
h.initial(2, 8, 0, 2, 0.01)
h.oscilate(12.56)

fig, axs = plt.subplots(nrows=1, ncols=3)

axs[0].plot(h.t, h.x)
axs[1].plot(h.t, h.vx)
axs[2].plot(h.t, h.ax)

axs[0].set_xlabel("t [s]")
axs[1].set_xlabel("t [s]")
axs[2].set_xlabel("t [s]")
axs[0].set_ylabel("x [m]")
axs[1].set_ylabel("v [m/s]")
axs[2].set_ylabel("a [m/s^2]")

plt.show()