from turtle import pd
import ProjectileDrop as pd
import matplotlib.pyplot as plt

p=pd.ProjectileDrop()
p.set_init(2000, 200)
p.drop()

plt.plot(p.x, p.y)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()
plt.plot(p.t, p.vy)
plt.xlabel('t [s]')
plt.ylabel('v_y [m/s]')
plt.show()