import numpy as np
import matplotlib.pyplot as plt

g = 9.80665
for i in range(0, 10872):
    y = np.load('Data/Pressure' + str(i) + '.npy')
    y = y * 133.32239023154
    y = ((y - 101020 - 1026 * g * 9)/(1026 * g))
    np.save('Data/Pressure' + str(i) + '.npy', y)
    print(i)
'''x = np.arange(0, len(y), 1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize = 20)
ax.plot(x, y, linewidth = 1, color='b')
ax = plt.gca()
ax.set_xlabel('Time, [sec.]', fontsize=20)
ax.set_ylabel('η(t), [m]', fontsize=20)
plt.axhline(y = 0, color = 'black', linewidth=0.5)
plt.show()'''