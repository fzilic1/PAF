import matplotlib.pyplot as plt

t=[]
x=[]
v=[]
a=[]
for line in open('podatci.txt', 'r'):
    lines = [i for i in line.split()]
    t.append(float(lines[0]))
    x.append(float(lines[1]))
    v.append(float(lines[2]))
    a.append(float(lines[3]))

plt.subplot(1, 3, 1)
plt.plot(t, x)
plt.xlabel('t [s]')
plt.ylabel('x [m]')

plt.subplot(1, 3, 2)
plt.plot(t, v)
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')

plt.subplot(1, 3, 3)
plt.plot(t, a)
plt.xlabel('t [s]')
plt.ylabel('a [m/s^2]')

plt.show()