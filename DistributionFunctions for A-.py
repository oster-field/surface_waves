import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(-10, 10, 0.001)
y = np.exp(-2*x*x)
ax.plot(x, y, color = 'black', alpha = 0.8, linestyle = '--', label = 'Rayleigh')
x = np.load('Numerical Data/xA- Gauss.npy')
y = np.load('Numerical Data/yA- Gauss.npy')
ax.scatter(x, y, s = 5, color='b', marker='^' , label='Gauss')
x = np.load('Numerical Data/xA- PM.npy')
y = np.load('Numerical Data/yA- PM.npy')
ax.scatter(x, y, s = 5, color='r', marker='o' , label='Pierson-Moskovitz')
x = np.load('xA- Nat.npy')
y = np.load('yA- Nat.npy')
ax.scatter(x, y, s = 5, color='g', marker='x' , label='Observational data')
ax = plt.gca()
ax.set_xlabel('A-/As', fontsize=20)
ax.set_ylabel('F(A-)', fontsize=20)

ax.vlines(2, -100, 100, color = 'dimgray', alpha = 0.6, linestyle = '--')
ax.tick_params(labelsize = 20)
ax.set(xlim = [0, 2.25], ylim = [0.000000063, 1])
ax.legend(fontsize=20)
#plt.yscale('log')
plt.show()