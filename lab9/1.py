#Куликов Н.В. ИУ7-13Б
#Даны массивы D и F. Сформировать матрицу A по формуле ajk = sin(dj+fk)
#Определить среднее арифметическое положительных чисел каждой строки
#матрицы и количество элементов, меньших среднего арифметического.
#Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
#виде матрицы и рядом столбцы AV и L.

from math import *

print('Введите элементы массива D через пробел, затем Enter')
d = [float(i) for i in input().split()]
print('Введите элементы массива F через пробел, затем Enter')
f = [float(i) for i in input().split()]

if len(d) == 0 and len(f) == 0:
    print('Массив не может быть пустым')
else:
    a = [[0.0] * len(f) for _ in range(len(d))]
    av = []
    l = []
    #Заполнение матрицы
    for i in range(len(d)):
        sr = 0           #Сумма положительных в ряду
        cnt = 0          #Кол-во положительных
        for j in range(len(f)):
            a[i][j] = sin(d[i] + f[j])
            if a[i][j] > 0:
                sr += a[i][j]
                cnt += 1

        if cnt > 0:
            av.append(sr / cnt)
        else:
            av.append(None)

    #Нахождение кол-ва элементов, меньших среднего арифметического ряда      
    for i in range(len(d)):
        cnt = 0
        if av[i] != None:
            for j in range(len(f)):
                if a[i][j] < av[i]:
                    cnt += 1        
            l.append(cnt)
        else:
            l.append(None)

    #Форматированный вывод матрицы
    len_matrix = 10*len(a[0])
    print(f'{"Матрица":^{len_matrix}} {"AV":^12} {"L":^10}')
    for i in range(len(d)):
        s = '|'
        for j in range(len(f)):
               s += f'{a[i][j]:^10.5g}'
        if av[i] != None:
            s += '|' + str(f'{av[i]:^10.5g}') + '| ' + f'{str(l[i]):^10}' + ' |'
        else:
            s += '|' + f'{str(av[i]):^10}' + '| ' + f'{str(l[i]):^10}' + ' |'
        print(s)
                
