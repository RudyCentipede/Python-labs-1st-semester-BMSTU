#Куликов Н.В. ИУ7-13Б
#Выполнить транспонирование квадратной матрицы

n = int(input('Введите кол-во строк в матрице: '))
if n < 0:
    print('Кол-во строк не может быть отрицательным')
else:
    #Заполнение матрицы
    a = []
    for i in range(n):
        print('Введите элементы',i+1, 'строки через пробел:', end = ' ')
        a.append([int(i) for i in input().split()])

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
    print('Измененная матрица') 
    tmp = f'{"":<3} '
    for j in range(n):
        tmp += f'{j+1:^6}'
    print(tmp)
        
    for i in range(n):
        tmp = f'{i+1:<3} '
        for j in range(n):
            tmp += f'{a[j][i]:^6}'
        print(tmp)
            
                 
                 
    
