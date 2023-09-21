import numpy as np
import matplotlib.pyplot as plt


y = np.arange(0)
Kw = 0
for i in range(0, 44361):
    print(i)
    y = np.load('20min_recordings/Rec' + str(i) + '.npy')
    if len(y) != 0:
        x = np.arange(0, len(y), 1)
        H = np.load('20min_recordings/MiA' + str(i) + '.npy')
        Hs = np.load('20min_recordings/As' + str(i) + '.npy')
        for j in range(0, len(H)):
            if H[j] < -2.2 * Hs:
                print(j)
                print(i)
                Kw = Kw + 1
                '''fig = plt.figure()
                ax = fig.add_subplot(111)
                ax.tick_params(labelsize=20)
                ax = plt.gca()
                ax.set_xlabel('Time, [sec.]', fontsize=20)
                ax.set_ylabel('η(t), [m]', fontsize=20)
                ax.axhline(y=0, color='black', linewidth=0.5)
                plt.title(label='Hs = ' + str(np.round(Hs, 3)) + '  H = ' + str(np.round(H[j], 3)), fontsize=20)
                ax.plot(x, y, linewidth=1, color='b')
                plt.show()'''
print(Kw)