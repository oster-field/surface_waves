import numpy as np

for j in range(7682, 7858):
    a = np.load('Data/Temperature' + str(j) + '.npy')
    for i in range(0, 5001):
        a = np.delete(a, [0])
    np.save('Data/Temperature' + str(j) + '.npy', a)

"""a = np.load('Data/Temperature6039.npy')
for i in range(0, 2801):
    a = np.delete(a, [0])
print(a)
np.save('Data/Temperature6039.npy', a)"""