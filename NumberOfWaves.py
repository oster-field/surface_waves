import numpy as np

up = 0
down = 0
for i in range(0, 44361):
    print(i)
    up = up + len(np.load('20min_recordings/Lup' + str(i) + '.npy'))
    down = down + len(np.load('20min_recordings/Ldown' + str(i) + '.npy'))
print('Up = ' + str(up))
print('Down = ' + str(down))