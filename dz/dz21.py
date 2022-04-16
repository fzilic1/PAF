import ngibanje as ng
import matplotlib.pyplot as plt

t=0.1
T=[]
X=[]
while t<12:
    T.append(t)
    X.append(ng.pos(2, 0, 2, t, 0.0001, 0, -5, 0, 0))
    t+=0.1
plt.plot(T, X)
plt.xlabel('t [s]')
plt.ylabel('x [s]')
plt.show()

t=0.1
T=[]
V=[]
while t<12:
    T.append(t)
    V.append(ng.vel(0, 0, 2, t, 0.0001, 0, 0, 0, 6))
    t+=0.1
plt.plot(T, V)
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.show()
