#Куликов Н.В. ИУ7-13Б
#Сформировать матрицу C путём построчного перемножения матриц A и B
#одинаковой размерности (элементы в i-й строке матрицы A умножаются на
#соответствующие элементы в i-й строке матрицы B), потом сложить все
#элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
#A, B, C и массив V

n = int(input('Введите кол-во строк в матрице A и B (1 число): '))
s = int(input('Введите кол-во столбцов в матрице A и B (1 число): '))

if n <= 0 or s <= 0:
    print('Кол-во столбцов и строк должно быть положительно')
else:
    #Заполнение матрицы
    print('Заполнение матрицы A')
    a = [[]] * n
    for i in range(n):
        print('Введите элементы', i + 1, 'строки через пробел: ',  end = '')
        a[i] = [float(k) for k in input().split()]

    print('Заполнение матрицы B')
    b = [[]] * n
    for i in range(n):
        print('Введите элементы', i + 1, 'строки через пробел: ',  end = '')
        b[i] = [float(k) for k in input().split()]

    #Проверка корректности ввода
    t = True
    for i in range(n):
        if len(a[i]) != s or len(b[i]) != s:
            t = False

    if t:
        #Формирование матрицы C
        c = [[0.0] * s for _ in range(n)]
        for i in range(n):
            for j in range(s):
                c[i][j] = a[i][j] * b[i][j]
                
        #Формирование массива V
        v = []
        for j in range(s):
            su = 0
            for i in range(n):
                su += c[i][j]
            v.append(su)

        #Вывод результата
        print('Mатрица A')
        for i in range(n):
            st = ''
            for j in range(s):
                st += str(f'{a[i][j]:.5g}') + ' '
            print(st)
        print()
        print('Mатрица B')
        for i in range(n):
            st = ''
            for j in range(s):
                st += str(f'{b[i][j]:.5g}') + ' '
            print(st)
        print()
        print('Mатрица C')
        for i in range(n):
            st = ''
            for j in range(s):
                st += str(f'{c[i][j]:.5g}') + ' '
            print(st)
        print()
        print('Массив V:', v)
    else:
        print('Некорректный ввод матрицы')
