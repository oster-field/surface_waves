import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq, rfft, rfftfreq, irfft

y = np.arange(0)
for i in range(3014, 6028):
    y = np.append(y, np.load('Data/Pressure' + str(i) + '.npy'))
    print(i)
Sensor_Frequency = 1
Record_Duration = len(y)
N = Sensor_Frequency * Record_Duration
s = rfft(y)
x = rfftfreq(N, (1/Sensor_Frequency)/(2*np.pi))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.tick_params(labelsize = 20)
#Spectra plotting
ax.plot(x, np.abs(s)/(len(y)/2), linewidth = 1, color='b')
#Cutting lower frequency componenst
#Before cutting
#ax.plot(np.arange(0, len(y), 1), y)
for i in range(0, len(s)):
    if x[i] < 0.00523598:
        s[i] = 0
y = irfft(s)
q = np.arange(0)
counter = 25027
'''for i in range(0, len(y)):
    q = np.append(q, y[i])
    if len(q) == 1200:
        np.save('20min_recordings/Rec' + str(counter) + '.npy', q)
        counter = counter + 1
        q = np.arange(0)'''
#After cutting
#ax.plot(np.arange(0, len(y), 1), y)
ax = plt.gca()
ax.set(xlim = [0, np.max(x)],
       ylim = [0, 0.0012])
ax.set_xlabel('ω, [rad/sec]', fontsize=20)
ax.set_ylabel('Amplitude, [m]', fontsize=20)
plt.show()