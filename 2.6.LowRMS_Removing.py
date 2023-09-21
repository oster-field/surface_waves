'''Удаление записей с почти нулевым волнением, на поверхности лежал лед'''
import numpy as np
import math

def rmsValue(arr, n):
    square = 0
    for i in range(0, n):
        square += (arr[i] ** 2)
    mean = (square / (float)(n))
    root = math.sqrt(mean)
    return root

for j in range(0, 44361):
    print(j)
    a = np.load('20min_recordings/Rec' + str(j) + '.npy')
    if rmsValue(a, len(a)) < 0.05:
        for i in range(0, len(a)):
            a = np.delete(a, [0])
    np.save('20min_recordings/Rec' + str(j) + '.npy', a)
