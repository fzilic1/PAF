import particle as prt
import numpy as np

p1=prt.Particle()
p1.set_initial_conditions(5, 30, 2, 0, 0.01)

D_ana=((5**2)*np.sin(2*30*np.pi/180)/9.81)+2
D_num=p1.range()
print (D_ana)
print (D_num)
Err=abs(D_ana-D_num)/D_ana
print (Err)

p1.reset()
p1.set_initial_conditions(5, 30, 2, 0, 0.01)