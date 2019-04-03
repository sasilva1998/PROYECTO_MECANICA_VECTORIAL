import beammech as bm
import numpy as np
import matplotlib.pyplot as plt
beam = {}
beam['length'] = 15000
beam['supports'] = (0, 15000)

L1 = bm.Load(force=-2, pos=5000)
L2 = bm.Load(force=-4, pos=10000)
L3 = bm.MomentLoad(moment=5000, pos=0)
beam['loads'] = [L1, L2,L3]
x=np.linspace(0,15,15001)
y=np.zeros(15001)
print(bm.solve(beam).get("R")[0].shear(15000)[0])
print(bm.solve(beam).get("R")[1].shear(15000)[15000])
plt.plot(x, bm.solve(beam).get("M"))
plt.plot(x,y)
plt.show()
