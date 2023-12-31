'''Программа моделирует случайное волновое поле с гауссовым спектром, обратное преобразование Фурье'''
import numpy as np
import matplotlib.pyplot as plt
import random
from PyAstronomy import pyaC
from scipy.stats import kurtosis, skew
##Определение физических констант
w0 = 0.7
K = 0.04
Q = 0.005625/(np.sqrt(2*np.pi)*K)
WDT = 11
N = 2**12
dt = 2*np.pi/WDT
dw = WDT/N
L = dt*N
print('dw = ' + str(dw)) #шаг по частоте
print('dt = ' + str(dt)) #шаг по времени
print('L = ' + str(L)) #длина записи
x = np.arange(0, L, dt, dtype=np.float64)
for counter in range(0, 1000): #в цикле происходит сумма гармоник со случайными фазами и спектральными амплитудами
    y = 0
    w = 0
    SkG = np.arange(0)
    Sp = np.arange(0)
    Der = np.arange(0)
    for i in range(0, N):
        w = w + dw #шаг по спектру
        v = random.uniform(0, 2*np.pi) #случайная фаза (равномерное распределение)
        S = Q*np.exp(-((w-w0)**2)/(2*K**2)) #спектральная амплитуда (коэффициент в фурье-пространстве)
        MonochromaticWave = (np.sqrt(2*dw*S))*(np.cos(w*x+v)) #каждая из гармоник в общей сумме
        y = y + MonochromaticWave
        #проверка качества каждой гармоники и уже имеющейся на данной итерации суммы:
        SkG = np.append(SkG, skew(y))
        Sp = np.append(Sp, S)
        Der = np.append(Der, np.abs(MonochromaticWave[0]-MonochromaticWave[len(MonochromaticWave)-1]))
    np.save('S(w)Gauss/etta ' + str(counter), y) #сохранение реализации поля для дальнейшего анализа в другой программе
    '''Визуализация проверки качества'''
    xS = np.arange(0, len(SkG), 1)
    xSp = np.arange(0, len(Sp), 1)
    xDer = np.arange(0, len(Der), 1)
    plt.plot(xS*dw, SkG, xSp*dw, Sp, xDer*dw, Der)
    '''График покажет статистические моменты, спектр и разницу в значениях на начале и конце каждой гармоники'''
    plt.show()
    q = np.arange(0)
    ymax = np.arange(0)
    ymin = np.arange(0)
    ym = 0
    yl = 0
    n = 0
    '''Выделение индивидуальных волн в записи методом пересечения нуля: 
    в полученном сете точек появляются точки, соединяющие ближайшие положительные и отрицательные
    в случае если есть переход нуля. Точки ставятся с ординатой в точности равной нулю.
    Таким образом появляется граница между отрицательными выбросами и положительными.'''
    xc, xi = pyaC.zerocross1d(x, y, getIndices=True)
    xnew = np.sort(np.append(x, xc))
    for i in range(1, len(xnew+1)):
        if (xnew[i] in xc):
            xzm1 = np.where(xnew == xnew[i-1])[0]
            yzm1 = np.where(y == y[xzm1])[0]
            y = np.insert(y, yzm1 + 1, [0])
    q = np.arange(0)
    for j in y:
        if j == 0:
            if q[len(q)-1] > 0:
                ymax = np.append(ymax, np.max(q))
            else:
                ymin = np.append(ymin, np.min(q))
            q = np.arange(0)
        q = np.append(q, j)
    np.save('S(w)Gauss/plus amplitudes ' + str(counter), ymax)
    np.save('S(w)Gauss/minus amplitudes ' + str(counter), ymin)
    #Создание массива содержащего высоты волн: сумма абсолютных значений положительных и отрицательных амплитуд
    wavelenght = np.arange(0)
    if len(ymax)>=len(ymin):
        for i in range(0, len(ymin)):
            wavelenght = np.append(wavelenght, [ymax[i] + abs(ymin[i])])
    if len(ymax)<len(ymin):
        for i in range(0, len(ymax)):
            wavelenght = np.append(wavelenght, [ymax[i] + abs(ymin[i])])
    np.save('S(w)Gauss/lenghts ' + str(counter), wavelenght)

