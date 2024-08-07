#Куликов Н.В. ИУ7-13Б
#Найти максимальное значение в квадратной матрице над главной диагональю и
#минимальное - под побочной диагональю.

n = int(input('Введите кол-во строк в матрице: '))
if n < 0:
    print('Кол-во строк не может быть отрицательным')
else:
    #Заполнение матрицы
    a = []
    for i in range(n):
        print('Введите элементы',i+1, 'строки через пробел:', end = ' ')
        a.append([int(i) for i in input().split()])
        
     #Проверка корректности ввода матрицы
    t = True
    for i in range(n):
        if n != len(a[i]):
            t = False

    if t:
        
        ma = 0
        mi = a[n-1][n-1]

        for i in range(n):
            for j in range(n):
                if i < j:
                    if ma < a[i][j]:
                        ma = a[i][j]
                if i + j >= n:
                    if mi > a[i][j]:
                        mi = a[i][j]
        
        
##        for i in range(n-1):
##            for k in range(1, n):
##                if a[i][k] > ma:
##                    print(ma)
##                    ma = a[i][k]
##                    print(ma)
##                    print('----')
##
##        for i in range(n):
##            j = 0
##            for k in range(j+1):
##                print(a[i][k])
##                if a[i][k] < mi:
##                    mi = a[i][k]
##
##            j += 1
        print('Максимальное значение над главной диагональю:', ma)
        print('Минимальное значение под побочной диагональю', mi)
            
        
    else:
        print('Некорректный ввод матрицы (должна быть квадратной))')
