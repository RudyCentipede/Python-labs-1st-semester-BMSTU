#Куликов Н.В. ИУ7-13Б
#Подсчитать в каждой строке матрицы D количество элементов, превышающих
#суммы элементов соответствующих строк матрицы Z. Разместить эти
#количества в массиве G, умножить матрицу D на максимальный элемент
#массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
#также массив G

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
        n_z = int(input('Введите кол-во строк в матрице Z: '))
        s_z = int(input('Введите кол-во столбцов в матрице Z: '))
        
        if n_d <= 0 or s_d <= 0:
            print('Кол-во столбцов и строк должно быть положительно')
        else:
            #Заполнение матрицы Z
            z = [[]] * n_z
            for i in range(n_z):
                print('Введите элементы', i + 1, 'строки через пробел: ',  end = '')
                z[i] = [float(k) for k in input().split()]

            t = True
            for i in range(n_z):
                if len(z[i]) != s_z:
                    t = False
            if t:
                #Считаем суммы строк матрицы Z
                sum_z = []
                for i in range(n_z):
                    subsum = 0
                    for j in range(s_z):
                        subsum += z[i][j]
                    sum_z.append(subsum)
                
                g = []
                #Подсчёт кол-ва элементов в строке матрицы D,
                #больших суммы эл-нтов соотв. строк матрицы Z
                if n_d <= n_z:
                    for i in range(n_d):
                        cnt = 0
                        for j in range(s_d):
                            if d[i][j] > sum_z[i]:
                                cnt += 1
                        g.append(cnt)
                else:
                    for i in range(n_z):
                        cnt = 0
                        for j in range(s_d):
                            if d[i][j] > sum_z[i]:
                                cnt += 1
                        g.append(cnt)
                
                print('Исходная матрица D')
                for i in range(n_d):
                    s = ''
                    for j in range(s_d):
                        s += str(f'{d[i][j]:.5g}') + ' '
                    print(s)
                print()
                #Поиск максимального эл-нта массива G
                ma = 0
                for i in g:
                    if i > ma:
                        ma = i
                #Умножение матрицы D на максимальный эл-нт массива G
                for i in range(n_d):
                    for j in range(s_d):
                        d[i][j] = d[i][j] * ma

                print('Измененная матрица D')
                for i in range(n_d):
                    s = ''
                    for j in range(s_d):
                        s += str(f'{d[i][j]:.5g}') + ' '
                    print(s)
                print()

                print('Матрица Z')
                for i in range(n_z):
                    s = ''
                    for j in range(s_z):
                        s += str(f'{z[i][j]:.5g}') + ' '
                    print(s)
                print()

                print('Массив G:', g)
                
            else:
                print('Некорректный ввод матрицы')
    else:
        print('Некорректный ввод матрицы')
