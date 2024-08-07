#Куликов Н.В. ИУ7-13Б
#Дана матрица символов. Заменить в ней все гласные английские буквы на
#точки. Напечатать матрицу до и после преобразования.


n = int(input('Введите кол-во строк в матрице: '))
s = int(input('Введите кол-во столбцов в матрице: '))

if n <= 0 or s <= 0:
    print('Кол-во столбцов и строк должно быть положительно')
else:
    #Заполнение матрицы
    d = [[]] * n
    for i in range(n):
        print('Введите элементы', i + 1, 'строки через пробел: ',  end = '')
        d[i] = [k for k in input().split()]

    #Проверка корректности ввода
    t = True
    for i in range(n):
        if len(d[i]) != s:
            t = False
        for j in range(s):
            if len(d[i][j]) > 1:
                t = False
    if t:
        print('Исходная матрица')
        for i in range(n):
            st = ''
            for j in range(s):
                st += str(d[i][j]) + ' '
            print(st)
            
        #Замена английских гласных букв на точки
        for i in range(n):
            for j in range(s):
                if d[i][j] in 'AEUOIYaeuoiy':
                    d[i][j] = '.'

        print('Измененная матрица')
        for i in range(n):
            st = ''
            for j in range(s):
                st += str(d[i][j]) + ' '
            print(st)

    else:
        print('Некорректный ввод матрицы')
