import numpy as np

a = np.arange(0)
for i in range(0, 44361):
    print(i)
    a = np.append(a, np.load('20min_recordings/Lup' + str(i) + '.npy')/(np.load('20min_recordings/Hs' + str(i) + '.npy')))
y = np.flipud(np.linspace(1/len(a), 1, len(a)))

x = np.sort(a)
np.save('xH Nat', x)
np.save('yH Nat', y)