import Planet as pl
import Universe as uni
import numpy as np

Sunce=pl.Planet()
Zemlja=pl.Planet()
Mars=pl.Planet()
Venera=pl.Planet()
Merkur=pl.Planet()
Komet=pl.Planet()

Sunce.initial(0, 0, 0, 0, 1.989*np.power(10.0, 30), 'yellow')
Mars.initial(0, 2.279*np.power(10.0, 11), 24070.0, 0, 6.39*np.power(10.0, 23), 'red')
Zemlja.initial(0, 1.486*np.power(10.0, 11), 29783.0, 0, 5.9742*np.power(10.0, 24), 'blue')
Venera.initial(0, 1.08*np.power(10.0, 11), 35020.0, 0, 4.867*np.power(10.0, 24), 'violet')
Merkur.initial(0, 0.697*np.power(10.0, 11), 47362.0, 0, 3.285*np.power(10.0, 24), 'orange')
Komet.initial(3.0*np.power(10.0, 11), 3.0*np.power(10.0, 11), -15000.0, 0.6*np.pi/4, 1.0*np.power(10.0, 14), 'brown')

p=uni.Universe()
p.initial(6)
p.addplanet(Sunce)
p.addplanet(Zemlja)
p.addplanet(Mars)
p.addplanet(Venera)
p.addplanet(Merkur)
p.addplanet(Komet)
p.evolve(0.8*31556908.8)