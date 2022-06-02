import Planet as pl
import Inter as int
import numpy as np

S=pl.Planet()
Z=pl.Planet()

S.initial(0, 0, 0, 1.989*np.power(10.0, 30))
Z.initial(0, 1.486*np.power(10.0, 11), 29783, 5.9742*np.power(10.0, 24))

p=int.Inter()
p.initial(1)
p.addplanet(S)
p.addplanet(Z)
p.inter(31556908.8)