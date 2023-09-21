'''Удаление т.н. спайков, которые обусловлены небольшими глюками оборудования'''
import numpy as np

for j in range(0, 44361):
    print(j)
    y = np.load('20min_recordings/Rec' + str(j) + '.npy')
    Hs = np.load('20min_recordings/Hs' + str(j) + '.npy')
    if len(y) != 0:
        for i in range(0, len(y)-1):
            if np.abs(y[i+1]-y[i]) > 1.5 * Hs:
                print('Spike removed')
                y[i+1] = (y[i] + y[i + 2])/2
    np.save('20min_recordings/Rec' + str(j) + '.npy', y)
