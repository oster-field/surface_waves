'''Проверка данных численой модели'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize=20)
ax.set(ylim=[0.00001, 1])
y = np.load('2022/etta 600.npy')
plt.xlim(left=np.min(y)/np.sqrt(np.var(y)), right=np.max(y)/np.sqrt(np.var(y)))
rndwv = np.arange(0)
sigma = np.sqrt(np.var(y))
for i in range(0, len(y)):
    y[i] = y[i] / sigma
    rndwv = np.append(rndwv, 1 - i / len(y))
y = np.sort(y)
xgauss = np.arange(-5, 5, 0.01)
gauss = ss.norm.cdf(-xgauss, loc=np.mean(y), scale=np.sqrt(np.var(y)))
ax.xaxis.set_major_formatter('{x}σ')
ax.scatter(y, rndwv, s=1, c='b')
ax.plot(xgauss, gauss, color='black', alpha=0.8, linestyle='--')
ax.vlines(1.5, 0, 1, color='dimgray', alpha=0.6, linestyle='--')
y = np.load('2022/etta 601.npy')
rndwv = np.arange(0)
for i in range(0, len(y)):
    y[i] = y[i] / np.sqrt(np.var(y))
    rndwv = np.append(rndwv, 1 - i / len(y))
y = np.sort(y)
ax.scatter(y, rndwv, s=1, c='r')
y = np.load('2022/etta 602.npy')
rndwv = np.arange(0)
for i in range(0, len(y)):
    y[i] = y[i] / np.sqrt(np.var(y))
    rndwv = np.append(rndwv, 1 - i / len(y))
y = np.sort(y)
ax.scatter(y, rndwv, s=1, c='g')

ax.set_xlabel('η/σ', fontsize=20)
ax.set_ylabel('F(η)', fontsize=20)
ax = plt.gca()
#plt.yscale('log')
plt.show()
