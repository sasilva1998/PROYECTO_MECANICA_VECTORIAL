import beammech as bm
import numpy as np
import matplotlib.pyplot as plt
beam = {}
largo=2.5
beam['length'] = largo*1000
beam['supports'] = None

L1 = bm.Load(force=-20, pos=500)
L2 = bm.Load(force=-30, pos=1000)
L3 = bm.Load(force=15, pos=2500)
L4 = bm.MomentLoad(moment=-10000, pos=1500)

beam['loads'] = [L1,L2,L3,L4]

x=np.linspace(0,2.5,2501)
y=np.zeros(2501)
#print(bm.solve(beam).get("R")[0].shear(2500)[0])
#print(bm.solve(beam).get("R")[1].shear(2500)[2500])
plt.plot(x, bm.solve(beam).get("M"))
plt.plot(x,y)
plt.show()
