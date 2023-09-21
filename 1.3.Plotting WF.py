import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

y = np.load('S(w)Gauss/etta 0.npy')
WDT = 11
N = 2**12
dt = 2*np.pi/WDT
dw = WDT/N
L = dt*N
x = np.arange(0, L, dt, dtype=np.float64)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim = [0, 1300],
       ylim = [-0.4, 0.4])
ax.tick_params(labelsize = 20)
ax = plt.gca()
print("Ассиметрия: " + str(skew(y)))
print("Среднее поле: " + str(np.mean(y)))
print("Эксцесс: " + str(kurtosis(y)))
ax.set_xlabel('t, [sec.]', fontsize=20)
ax.set_ylabel('η(x = 0, t), [m]', fontsize=20)
ax.plot(x, y, color='b')
plt.show()
