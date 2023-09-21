import numpy as np
import matplotlib.pyplot as plt
def comparison_by_spectra(AH, Nr_start1, Nr_end1, s1, marker1, c1, Nr_start2, Nr_end2, s2, marker2, c2):
    #Параметры изображения
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(AH + '/' + AH + 's', fontsize=20)
    ax.set_ylabel('F(' + AH + ')', fontsize=20)
    ax.set(xlim = [0, 3], ylim = [0.000000063, 1])
    ax.tick_params(labelsize = 20)
    if AH == 'H':
        name = 'lenghts'
        Significant = 0.3
    elif AH == 'A+':
        name = 'plus amplitudes'
        Significant = 0.15
    elif AH == 'A-':
        name = 'minus amplitudes'
        Significant = -0.15
    # Достаем и объединяем массивы
    wln = np.arange(0)
    for i in range(Nr_start1, Nr_end1):
        wln = np.append(wln, np.load('S(w)Gauss/' + name + ' ' + str(i) + '.npy'))
    rndwv = np.arange(0)
    for i in range(0, len(wln)):
        wln[i] = wln[i] / Significant
        rndwv = np.append(rndwv, 1 - i/len(wln))
    wln = np.sort(wln)
    ax.scatter(wln, rndwv, c = c1, s=s1, label = 'Gauss', marker = marker1)
    #Объем данных большой, считается довольно долго, при желании можно сохранить чтобы в следующий раз построить без рассчета
    '''np.save('xA+ Gauss', wln)
    np.save('yA+ Gauss', rndwv)'''
    wln = np.arange(0)
    rndwv = np.arange(0)
    for i in range(Nr_start2, Nr_end2):
        wln = np.append(wln, np.load('S(w)PM/' + name + ' ' + str(i) + '.npy'))
    for i in range(0, len(wln)):
        wln[i] = wln[i] / Significant
        rndwv = np.append(rndwv, 1 - i / len(wln))
    wln = np.sort(wln)
    ax.scatter(wln, rndwv, c = c2, s=s2, label = 'Pierson-Moskovitz', marker = marker2)
    '''np.save('xA+ PM', wln)
    np.save('yA+ PM', rndwv)'''
    #Рэлей
    x = np.arange(-10, 10, 0.001)
    ralaigh = np.exp(-2*x*x)
    ax.plot(x, ralaigh, color = 'black', alpha = 0.8 , linestyle = '--', label = 'Rayleigh distribution')
    ax.vlines(2, x.min(), x.max(), color = 'dimgray', alpha = 0.6 , linestyle = '--')
    ax = plt.gca()
    ax.legend(fontsize = 15)
    plt.yscale('log')
    plt.show()

comparison_by_spectra('H', 0, 100, 5, 'X', 'b', 0, 100, 5, '^', 'r')
comparison_by_spectra('A-', 500, 700, 5, 'X', 'b', 500, 700, 5, '^', 'r')