import Projectile as pr
import matplotlib.pyplot as plt

p=pr.Projectile()
p.set_initial_conditions(15, 60, 0, 0, 1, 1.225, 0.35, 0.5, 0.01)

p.plot_trajectory('RK')
p.reset()
p.set_initial_conditions(15, 60, 0, 0, 1, 1.225, 0.35, 0.5, 0.01)
p.plot_trajectory()
plt.show()