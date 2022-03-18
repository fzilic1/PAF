import particle as prt
import numpy as np

p1=prt.Particle()
v0=5
alpha=30
x0=3
y0=10
dt=0.01

p1.set_initial_conditions(v0, alpha, x0, y0, dt)

D_ana = (v0 * np.cos(alpha*np.pi/180) * (v0 * np.sin(alpha*np.pi/180) + np.sqrt((v0 * np.sin(alpha*np.pi/180))**2 + 2 * 9.81 * y0)) / 9.81)+x0
D_num=p1.range()

print (D_ana)
print (D_num)
Err=abs(D_ana-D_num)/D_ana
print(Err)