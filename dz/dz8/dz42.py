import Projectile as pr
import matplotlib.pyplot as plt

p1=pr.Projectile()
p2=pr.Projectile()

print(p1.target(20, 0, 0, 2, 1.225, 0.4, 0.5, 5, 6, 0.5))
print(p2.target(30, 0, 0, 4, 1.225, 0.5, 0.5, 10, 10, 2))