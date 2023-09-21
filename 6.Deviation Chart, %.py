'''Программа строит графики отличия от референсного распределения для всего
готового набора реализаций'''
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize = 20)
ax.set_xlabel('A-/As', fontsize=20)
ax.set_ylabel('100% * |Fr - F|/Fr, [%]', fontsize=20)

y = np.arange(0)
for i in range(1000, 3000):
    y = np.append(y, np.load('S(w)Gauss/minus amplitudes ' + str(i) + '.npy'))
rndwv = np.arange(0)
print(len(y))
for i in range(0, len(y)):
    y[i] = y[i]/ -0.15
    rndwv = np.append(rndwv, 1 - i / len(y))
y = np.sort(y)
rayleigh = np.exp(-2*y*y)
erf = np.arange(0)
for i in range(0, len(y)):
    erf = np.append(erf, 100 * np.abs(rayleigh[i] - rndwv[i])/ rayleigh[i])
ax.plot(y, erf, marker = '.', linewidth = 1, label = 'Gauss')
z = np.arange(0)
for i in range(0, 2500):
    z = np.append(z, np.load('S(w)PM/minus amplitudes ' + str(i) + '.npy'))
rndwv = np.arange(0)
print(len(z))
for i in range(0, len(z)):
    z[i] = z[i]/ -0.15
    rndwv = np.append(rndwv, 1 - i / len(z))
z = np.sort(z)
rayleigh2 = np.exp(-2*z*z)
erf = np.arange(0)
for i in range(0, len(z)):
    erf = np.append(erf, 100 * np.abs(rayleigh2[i] - rndwv[i])/rayleigh2[i])
ax.plot(z, erf, marker = '.', linewidth = 1, color = 'r', label = 'Pierson-Moskovitz')
ax = plt.gca()
ax.legend(fontsize = 15)
ax.grid()
plt.xticks(np.arange(0, 3, 0.25))
plt.show()