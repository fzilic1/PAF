import particle as par
import matplotlib.pyplot as plt

p=par.Particle()
v0=10
theta=[]
t=[]
D=[]
alpha=0

while alpha<90:
    p.set_initial_conditions(v0, alpha, 0, 0, 0.01)
    theta.append(alpha)
    t.append(p.total_time())
    D.append(p.range())
    p.reset()
    alpha+=0.1

fig, (ax1, ax2) = plt.subplots(2, sharex=True)

ax1.plot(theta, t)
ax2.plot(theta, D)
ax1.set(ylabel='Trajanje gibanja [s]')
ax2.set(xlabel='theta [deg]', ylabel='Domet [m]')
plt.show()
