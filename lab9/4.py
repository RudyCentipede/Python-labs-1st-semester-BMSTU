#Куликов Н.В. ИУ7-13Б
#Задана матрица D и массив I, содержащий номера строк, для которых
#необходимо определить максимальный элемент. Значения максимальных
#элементов запомнить в массиве R. Определить среднее арифметическое
#вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
#среднее арифметическое значение.


n_d = int(input('Введите кол-во строк в матрице D: '))
s_d = int(input('Введите кол-во столбцов в матрице D: '))

if n_d <= 0 or s_d <= 0:
    print('Кол-во столбцов и строк должно быть положительно')
else:
    #Заполнение матрицы D
    d = [[]] * n_d
    for i in range(n_d):
        print('Введите элементы', i + 1, 'строки через пробел: ',  end = '')
        d[i] = [float(k) for k in input().split()]

    t = True
    for i in range(n_d):
        if len(d[i]) != s_d:
            t = False
    if t:
        print('Введите элементы массива I через пробел, затем нажмите Enter')
        l = [int(i) for i in input().split()]
        t = True
        for i in l:
            if not (0 < i <= n_d):
                t = False

        if t:
            #Формирование массива R из максимальных элементов строк
            r = []
            for i in l:
                ma = 0
                for j in range(s_d):
                    if d[i - 1][j] > ma:
                        ma = d[i - 1][j]
                r.append(ma)

            #Вычисление среднего арифметического
            su_r = 0   
            for i in r:
                su_r += i
            sr_r = su_r / len(r)
            
            #Вывод результатов
            print('Mатрица D')
            for i in range(n_d):
                s = ''
                for j in range(s_d):
                    s += str(f'{d[i][j]:.5g}') + ' '
                print(s)
            print()
            print('Массив l:', l)
            print('Массив R:', r)
            print('Cреднее арифметическое вычисленных максимальных значений:', f'{sr_r:.5g}')
            
            
        else:
            print('Массив l содержит числа, не соответствующие номерам строк матрицы')
        
    else:
        print('Некорректный ввод матрицы')
