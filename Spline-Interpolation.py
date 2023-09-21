import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

for i in range(0, 44361):
    y = np.load('20min_recordings/Rec' + str(i) + '.npy')
    if len(y) != 0:
        x = np.arange(0, len(y), 1)
        cs = CubicSpline(x, y)
        xs = np.arange(0, len(y), 0.25)
        print(i)
        np.save('20min_recordings/Rec' + str(i) + '.npy', cs(xs))
'''fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize = 20)
ax.plot(xs, cs(xs), linewidth = 1, color='b', marker='.' , label="With interpolation")
ax.plot(x, y, linewidth = 1, color='r', marker='.' , label='Without interpolation')
ax = plt.gca()
ax.set_xlabel('Time, [sec.]', fontsize=20)
ax.set_ylabel('η(t), [m]', fontsize=20)
ax.legend(fontsize=20)
plt.show()'''