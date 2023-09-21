import numpy as np
import matplotlib.pyplot as plt
'''Функция строит функции распределения высот или амплитуд в логарифмическом масштабе
в зависимости от числа реализаций входящих в усреднение функции распределения. На вход принимается
тип величины (высота или амплитуда), конкретные реализации: номер первой и последней из числа смоделированных
ранее, функции построены в безразмерных величинах (каждое значение делится на посчитанную заранее величину)
также строится график референсной кривой (Рэлееское распределение)'''
def plotting_function_by_Nr(AH, Nr_start, Nr_end, s, marker, c):
    #Задание параметров картинки
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.tick_params(labelsize=20)
    ax.set(ylim=[0.000000063, 1])
    plt.xlim(left=0)
    plt.xlim(right=3)
    ax.set_xlabel(AH + '/' + AH + 's', fontsize=20)
    ax.set_ylabel('F(' + AH + ')', fontsize=20)
    #Загрузка данных из модели
    wln = np.arange(0)
    if AH == 'H':
        name = 'lenghts'
        Significant = 0.3
    elif AH == 'A+':
        name = 'plus amplitudes'
        Significant = 0.15
    elif AH == 'A-':
        name = 'minus amplitudes'
        Significant = -0.15
    for i in range(Nr_start, Nr_end):
        wln = np.append(wln, np.load('S(w)Gauss/' + name + ' ' + str(i) + '.npy'))
    rndwv = np.arange(0)
    for i in range(0, len(wln)):
        wln[i] = wln[i] / Significant #Представление в безразмерных величинах
        rndwv = np.append(rndwv, 1 - i / len(wln)) #Множество значений функции распределения
    #Построение графика
    wln = np.sort(wln)
    x = np.arange(0, 1, 0.001)
    ax.vlines(2, x.min(), x.max(), color='dimgray', alpha=0.6, linestyle='--')
    ax.scatter(wln, rndwv, c=c, s=s, label=str(Nr_end-Nr_start) + ' realizations', marker=marker)
    #Построение Рэлеевской кривой
    xr = np.arange(-10, 10, 0.001)
    ralaigh = np.exp(-2 * xr * xr)
    ax.plot(xr, ralaigh, color='black', alpha=0.8, linestyle='--', label='Rayleigh distribution')
    ax = plt.gca()
    ax.legend(fontsize=15)
    plt.yscale('log')
    plt.show()
#Использование функции для разного набора реализаций:
plotting_function_by_Nr('H', 0, 100, 5, 'X', 'b')
plotting_function_by_Nr('A+', 0, 500, 5, 'X', 'r')
plotting_function_by_Nr('A-', 100, 900, 5, 'X', 'g')
