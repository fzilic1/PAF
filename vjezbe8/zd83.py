import Projectile as pr
import matplotlib.pyplot as plt

p1=pr.Projectile()
v0=20
theta=45
m=0.5
rho=1.225
C_d=0.01
A=0.2
dt=0.001

R=[]
C=[]

while(C_d<1):
    p1.set_initial_conditions(v0, theta, 0, 0, m, rho, C_d, A, dt)
    C.append(C_d)
    R.append(p1.range('RK'))
    p1.reset()
    C_d+=0.02

plt.plot(C, R)
plt.xlabel('C_d')
plt.ylabel('Domet [m]')
plt.show()


C_d=0.3
M=[]
Ri=[]

while(m<2):
    p1.set_initial_conditions(v0, theta, 0, 0, m, rho, C_d, A, dt)
    M.append(m)
    Ri.append(p1.range('RK'))
    p1.reset()
    m+=0.05

plt.plot(M, Ri)
plt.xlabel('m [kg]')
plt.ylabel('Domet [m]')
plt.show()