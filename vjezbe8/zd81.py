import Projectile as pr
import matplotlib.pyplot as plt

p1=pr.Projectile()
p2=pr.Projectile()
p1.set_initial_conditions(20, 45, 0, 0, 2, 1.225, 0.4, 0.5)
p2.set_initial_conditions(20, 45, 0, 0, 2, 1.225, 0, 0.5 )

p1.plot_trajectory()
p2.plot_trajectory()
plt.show()