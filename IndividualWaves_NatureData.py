import numpy as np
import matplotlib.pyplot as plt
from PyAstronomy import pyaC

fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize = 20)
ax.set_xlabel('Time, [sec.]', fontsize=20)
ax.set_ylabel('η(t), [m]', fontsize=20)



for counter in range(0, 44361):
    y = np.load('20min_recordings/Rec' + str(counter) + '.npy')
    if len(y) != 0:
        print(counter)
        x = np.arange(0, len(y), 1)
        sigma = np.sqrt(np.var(y))
        Hs = 4 * sigma
        Ams = 2 * sigma
        np.save('20min_recordings/Hs' + str(counter) + '.npy', Hs)
        np.save('20min_recordings/As' + str(counter) + '.npy', Ams)
        ydown = y
        q = np.arange(0)
        ymax = np.arange(0)
        ymin = np.arange(0)
        ym = 0
        yl = 0
        n = 0
        xc, xi = pyaC.zerocross1d(x, y, getIndices=True)
        Tz = 1200 / len(xc)
        np.save('20min_recordings/Tz' + str(counter) + '.npy', Tz)
        xnew = np.sort(np.append(x, xc))
        for i in range(1, len(xnew + 1)):
            if (xnew[i] in xc):
                xzm1 = np.where(xnew == xnew[i - 1])[0]
                yzm1 = np.where(y == y[xzm1])[0]
                y = np.insert(y, yzm1 + 1, [0])
        q = np.arange(0)
        for j in y:
            if j == 0:
                if q[len(q) - 1] > 0:
                    ymax = np.append(ymax, np.max(q))
                else:
                    ymin = np.append(ymin, np.min(q))
                q = np.arange(0)
            q = np.append(q, j)
        np.save('20min_recordings/PlA' + str(counter) + '.npy', ymax)
        np.save('20min_recordings/MiA' + str(counter) + '.npy', ymin)
        wavelenght = np.arange(0)
        if len(ymax) >= len(ymin):
            for i in range(0, len(ymin)):
                wavelenght = np.append(wavelenght, [ymax[i] + abs(ymin[i])])
        if len(ymax) < len(ymin):
            for i in range(0, len(ymax)):
                wavelenght = np.append(wavelenght, [ymax[i] + abs(ymin[i])])
        np.save('20min_recordings/Lup' + str(counter) + '.npy', wavelenght)
        y = ydown
        y = -1 * y
        q = np.arange(0)
        ymax = np.arange(0)
        ymin = np.arange(0)
        xc, xi = pyaC.zerocross1d(x, y, getIndices=True)
        xnew = np.sort(np.append(x, xc))
        for i in range(1, len(xnew + 1)):
            if (xnew[i] in xc):
                xzm1 = np.where(xnew == xnew[i - 1])[0]
                yzm1 = np.where(y == y[xzm1])[0]
                y = np.insert(y, yzm1 + 1, [0])
        q = np.arange(0)
        for j in y:
            if j == 0:
                if q[len(q) - 1] > 0:
                    ymax = np.append(ymax, np.max(q))
                else:
                    ymin = np.append(ymin, np.min(q))
                q = np.arange(0)
            q = np.append(q, j)
        wavelenght = np.arange(0)
        if len(ymax) >= len(ymin):
            for i in range(0, len(ymin)):
                wavelenght = np.append(wavelenght, [ymax[i] + abs(ymin[i])])
        if len(ymax) < len(ymin):
            for i in range(0, len(ymax)):
                wavelenght = np.append(wavelenght, [ymax[i] + abs(ymin[i])])
        np.save('20min_recordings/Ldown' + str(counter) + '.npy', wavelenght)
    else:
        print('0')
        np.save('20min_recordings/Hs' + str(counter) + '.npy', np.arange(0))
        np.save('20min_recordings/As' + str(counter) + '.npy', np.arange(0))
        np.save('20min_recordings/Tz' + str(counter) + '.npy', np.arange(0))
        np.save('20min_recordings/PlA' + str(counter) + '.npy', np.arange(0))
        np.save('20min_recordings/MiA' + str(counter) + '.npy', np.arange(0))
        np.save('20min_recordings/Lup' + str(counter) + '.npy', np.arange(0))
        np.save('20min_recordings/Ldown' + str(counter) + '.npy', np.arange(0))