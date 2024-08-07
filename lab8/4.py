#Куликов Н.В. ИУ7-13Б
#Переставить местами столбцы с максимальной и минимальной суммой элементов

n = int(input('Введите кол-во строк в матрице: '))
columm = int(input('Введите кол-во столбцов в матрице: '))
if n < 0:
    print('Кол-во строк не может быть отрицательным')
else:
    #Заполнение матрицы
    a = []
    for i in range(n):
        print('Введите элементы',i+1, 'строки через пробел:', end = ' ')
        a.append([int(i) for i in input().split()])
        
     #Проверка корректности ввода матрицы
    le = len(a[0])
    t = True
    for i in range(n):
        if le != len(a[i]):
            t = False

    if t:
        print('Исходнaя матрица')    
        tmp = f'{"":<3} '
        for j in range(n):
            tmp += f'{j+1:^6}'
        print(tmp)
        
        for i in range(n):
            tmp = f'{i+1:<3} '
            for j in range(n):
                tmp += f'{a[i][j]:^6}'
            print(tmp)
        print('\n')
    
        su_min = sum([int(a[i][0]) for i in range(n)])
        su_max = 0
        n_min = 0
        n_max = 0
        for i in range(columm):
            su = 0
            for j in range(n):
                su += a[j][i]
                
            if su < su_min:
                su_min = su
                n_min = i
                
            if su > su_max:
                su_max = su
                n_max = i

        for i in range(n):
            a[i][n_min], a[i][n_max] = a[i][n_max], a[i][n_min]
        print('Измененная матрица')    
        tmp = f'{"":<3} '
        for j in range(n):
            tmp += f'{j+1:^6}'
        print(tmp)
        
        for i in range(n):
            tmp = f'{i+1:<3} '
            for j in range(n):
                tmp += f'{a[i][j]:^6}'
            print(tmp)
        print('\n')
        
    else:
        print('Некорректный ввод матрицы')
