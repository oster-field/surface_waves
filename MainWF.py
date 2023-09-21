'''Построение графика по обработанным данным с датчика'''
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0)
for i in range(39541, 39543):
    y = np.append(y, np.load('20min_recordings/Rec' + str(i) + '.npy'))
    print(i)
x = np.arange(0, len(y), 1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize = 20)
ax.plot(x, y, linewidth = 1, color='b')
ax = plt.gca()
ax.set_xlabel('Time, [sec.]', fontsize=20)
ax.set_ylabel('η(t), [m]', fontsize=20)
ax.axhline(y = 0, color = 'black', linewidth=0.5)
plt.show()
