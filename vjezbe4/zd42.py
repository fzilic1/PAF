import calculus as cal
import matplotlib.pyplot as plt

def f1(x):
    return 6*x**3+x**2+3*x+1

print(cal.intlim(f1, -5, 5, 2000))
print(cal.numint(f1, -5, 5, 2000))

F=4.3333333
a=0
b=1
y1=[]
y2=[]
y3=[]
y4=[]
N=range(1, 200)

for i in N:
    y1.append(cal.intlim(f1, a, b, i)[0])
    y2.append(cal.intlim(f1, a, b, i)[1])
    y3.append(cal.numint(f1, a, b, i))
    y4.append(F)

plt.plot(N, y1, linestyle='dotted')
plt.plot(N, y2, linestyle='dotted')
plt.plot(N, y3, linestyle='dotted')
plt.plot(N, y4)
plt.xlabel('N')
plt.ylabel('integral')
plt.show()