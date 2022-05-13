import bungee as b
import matplotlib.pyplot as plt

b.bungee(150, 80, 10, 10, 0.7, 1, 1.225, 100)
b.bungee(150, 80, 10, 10, 0, 1, 1.225, 100)
plt.legend(['C=0.7', 'C=0'])
plt.show()

b.energy(150, 80, 10, 10, 0, 1, 1.225, 100)
plt.title('C=0')
plt.show()

b.energy(150, 80, 10, 10, 0.7, 1, 1.225, 100)
plt.title('C=0.7')
plt.show()