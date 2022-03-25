import calculus as cal
import math
import matplotlib.pyplot as plt

def f1(x):
    return 6*x**3+x**2+3*x+1

def f2(x):
    return math.sin(x)

print(cal.dev(f1, 4))
print(cal.dev(f2, 0))

a=-2
b=2
x=[]
y=[]

p1=cal.devrange(f1, a, b, 0.01)
p2=cal.devrange(f1, a, b, 0.2)

while a <= b:
    x.append(a)
    y.append(18*a**2+2*a+3)
    a+=0.01

plt.plot(x, y)
plt.plot(p1[0], p1[1], linestyle='--')
plt.plot(p2[0], p2[1], linestyle='-.')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot()
plt.show()