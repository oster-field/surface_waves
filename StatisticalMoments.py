import numpy as np
from scipy.stats import skew, kurtosis

y = np.arange(0)
c = 0
M = 0
D = 0
A = 0
K = 0
for i in range(0, 44361):
    print(i)
    y = np.load('20min_recordings/Rec' + str(i) + '.npy')
    if len(y) != 0:
        c = c + 1
        M = M + np.mean(y)
        D = D + np.var(y)
        A = A + skew(y)
        K = K + kurtosis(y)
print('Mean = ' + str(M/c))
print('Dispersion = ' + str(D/c))
print('Asimmetry = ' + str(A/c))
print('Kurtosis = ' + str(K/c))
print('As = ' + str(2*np.sqrt(D/c)))
print('Hs = ' + str(4*np.sqrt(D/c)))