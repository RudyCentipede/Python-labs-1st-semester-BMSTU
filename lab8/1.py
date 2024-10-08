#Куликов Н.В. ИУ7-13Б
#Найти строку, где Наименьшее количество чётных элементов.

n = int(input('Введите кол-во строк в матрице: '))
if n < 0:
    print('Кол-во строк не может быть отрицательным')
else:
    #Заполнение матрицы
    a = []
    for i in range(n):
        print('Введите элементы',i+1, 'строки через пробел:', end = ' ')
        a.append([int(i) for i in input().split()])

    cnt_res = n                     #наименьшее кол-во чётных элементов
    kol = 0                         #количество чётных элементов всего
    num = 0                         #номер интересующей строки
    for i in range(n):
        cnt = 0                     #кол-во четных элементов в строке
        for j in range(len(a[i])):
            if a[i][j] % 2 == 0:
                cnt += 1
                kol += 1
        #присвоение наименьшему кол-ву чётных значение текущего кол-ва
        #и присвоение текущего индекса номеру интересующей строки
        if cnt < cnt_res or kol == 1:
            cnt_res = cnt
            num = i
    if kol > 0:
        print('Наименьшее кол-во чётных элементов содержится в строке номер ', num + 1)
    else:
        print('В матрице нет чётных элементов')
