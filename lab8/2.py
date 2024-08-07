#Куликов Н.В. ИУ7-13Б
#Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.

n = int(input('Введите кол-во строк в матрице: '))
if n < 0:
    print('Кол-во строк не может быть отрицательным')
else:
    #Заполнение матрицы
    a = []
    for i in range(n):
        print('Введите элементы',i+1, 'строки через пробел:', end = ' ')
        a.append([int(i) for i in input().split()])

    ma = 0                #наибольшее кол-во отрицательных элементов
    mi = len(a[0])        #наименьшее кол-во отрицательных элементов
    n_ma = 0
    n_mi = 0
    kol = 0               #кол-во отрицательных элементов
    columm = 0            #кол-во колонок
    
    for i in range(n):
        cnt = 0
        for j in range(len(a[i])):
            if a[i][j] < 0:
                cnt += 1
                kol += 1
        if ma < cnt:
            ma = cnt
            n_ma = i
            
        if mi > cnt:
            mi = cnt
            n_mi = i
            
        if columm < len(a[i]):
            columm = len(a[i])

    print('Исходная матрица')    
    tmp = f'{"":<3} '
    for j in range(columm):
        tmp += f'{j+1:^6}'
    print(tmp)
        
    for i in range(n):
        tmp = f'{i+1:<3} '
        for j in range(columm):
            tmp += f'{a[i][j]:^6}'
        print(tmp)
            
    if kol > 0:
        #переставление строк
        a[n_mi], a[n_ma] = a[n_ma], a[n_mi]
        
        #форматированный вывод матрицы
        print('\n')
        print('Измененная матрица')
        tmp = f'{"":<3} '
        for j in range(columm):
            tmp += f'{j+1:^6}'
        print(tmp)
        
        for i in range(n):
            tmp = f'{i+1:<3} '
            for j in range(columm):
                tmp += f'{a[i][j]:^6}'
            print(tmp)
    else:
        print('Нет в матрице строк для замены')
    
