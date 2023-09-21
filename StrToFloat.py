import numpy as np

for i in range(0, 10872):
    a = np.load('Data/Temperature' + str(i) + '.npy')
    a = a.astype(float)
    np.save('Data/Temperature' + str(i) + '.npy', a)
    print(i)