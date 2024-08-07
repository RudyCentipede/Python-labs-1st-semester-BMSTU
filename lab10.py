#Куликов Н.В. ИУ7-13
#Программа для вычисления приближённого значения интеграла
#известной, заданной в программе, функции двумя разными методами:
#методом правых прямоугольников и методом трапеций

#Заданная функция
def f(x):
    return x**2

#Первообразная заданной функции
def F(x):
    return (x**3)/3

#Корректный ввод кол-ва участков разбиения
def correct_n_input(put):
    a = list(put)
    if a[0] != '0':
        if all(i in '1234567890' for i in a):
            return int(put)
##    print('Некорректный ввод')
##    exit()

#Корректный ввод начала и конца отрезка итегрирования
def correct_segment_input(put):
    a = list(put)
    if 'e' in a:
        return epsilon_check(put)
    if len(a) == 1 and a[0] in '1234567890':
        return float(put)
    elif len(a) > 1:
        if a[0] != '0' or a[1] == '.':
            if all(i in '1234567890' for i in a) or a[1] == '.' and a.count('.') == 1 and all(i in '1234567890.' for i in a):
                return float(put)
##    print('Некорректный ввод')
##    exit()

#Корректный ввод погрешности
def epsilon_check(put):
    if 'e' in put:
        a = list(put.split('e'))
    else:
        return correct_segment_input(put)
    if len(a) == 2 and a[1][0] in '+-':
        fir = a[0]
        sec = a[1]
        t_fir = False
        t_sec = False
        if len(fir) == 1 and fir[0] in '1234567890':
            t_fir = True
        elif fir[0] != '0' or fir[1] == '.':
            if all(i in '1234567890' for i in fir) or fir[1] == '.' and fir.count('.') == 1 and all(i in '1234567890.' for i in fir):
                t_fir = True
        if all(sec[i] in '1234567890' for i in range(1, len(sec))):
            t_sec = True

        if t_fir and t_sec:
            return float(put)      
##    print('Некорректный ввод')
##    exit()
    

#Метод правых прямоугольников
def right_rectangle(end, start, n):
    h = (end - start) / n
    subst = start + h
    s = 0
    while subst <= end:
        s += (f(subst) * h)
        subst += h
    return s

#Метод трапеций
def trapezoid(end, start, n):
    h = (end - start) / n
    subst = start + h
    s = 0
    while subst <= end:
        s += ((f(subst - h) + f(subst)) * h / 2)
        subst += h
    return s

#Абсолютная погрешность
def delta_absolute(current, real):
    return current - real

#Относительная погрешность
def delta_relative(delta, real):
    return (delta / real) * 100
    
                
#Ввод значений пользователем
start, end, n1, n2 = None, None, None, None
while start is None or end is None or n1 is None or n2 is None:
    start = correct_segment_input(input('Введите начало отрезка интегрирования: '))
    end = correct_segment_input(input('Введите конец отрезка интегрирования: '))
    n1 = correct_n_input(input('Введите кол-во участков разбиения N1: '))
    n2 = correct_n_input(input('Введите кол-во участков разбиения N2: '))
    if start is None or end is None or n1 is None or n2 is None:
        print('Некорректный ввод')
if end > start:
    #Действительное значение интеграла
    real_integral = F(end) - F(start)

    #Метод правых прямоугольников
    s1 = right_rectangle(end, start, n1)
    s2 = right_rectangle(end, start, n2)

    #Метод трапеций
    s3 = trapezoid(end, start, n1)
    s4 = trapezoid(end, start, n2)

    #Вывод таблицы
    print('-' * 40)
    print(f'| {" ":10} | {"N1":^10} | {"N2":^10} |')
    print('-' * 40)
    print(f'| {"Метод 1":^10} | {s1:^10.5g} | {s2:^10.5g} |')
    print(f'| {"Метод 2":^10} | {s3:^10.5g} | {s4:^10.5g} |')
    print('-' * 40)

    #Расчет и вывод погрешностей
    d_a1 = abs(delta_absolute(s1, real_integral))
    d_a2 = abs(delta_absolute(s2, real_integral))
    d_a3 = abs(delta_absolute(s3, real_integral))
    d_a4 = abs(delta_absolute(s4, real_integral))
    number_mi = 0
    mi = d_a1
    number_ma = 0
    ma = d_a1
    tick = 0
    for i in d_a1, d_a2, d_a3, d_a4:
        tick += 1
        if i < mi:
            mi = i
            number_mi = tick
        if i > ma:
            ma = i
            number_ma = tick

    print('1 измерение:', 'Aбсолютная погрешность:', f'{delta_absolute(s1, real_integral):.5g}', '  Oтносительная погрешность:', f'{delta_relative(delta_absolute(s1, real_integral), real_integral):.5g}')
    print('2 измерение:', 'Aбсолютная погрешность:', f'{delta_absolute(s2, real_integral):.5g}', '  Oтносительная погрешность:', f'{delta_relative(delta_absolute(s2, real_integral), real_integral):.5g}')
    print('3 измерение:', 'Aбсолютная погрешность:', f'{delta_absolute(s3, real_integral):.5g}', '  Oтносительная погрешность:', f'{delta_relative(delta_absolute(s3, real_integral), real_integral):.5g}')
    print('4 измерение:', 'Aбсолютная погрешность:', f'{delta_absolute(s4, real_integral):.5g}', '  Oтносительная погрешность:', f'{delta_relative(delta_absolute(s4, real_integral), real_integral):.5g}')
    if number_mi == 1 or number_mi == 2:
        print('Наиболее точнен 1 метод')
        worst = trapezoid
    else:
        print('Наиболее точнен 2 метод')
        worst = right_rectangle


    #Расчет и вывод приближенного значения интеграла и количества отрезков, необходимых для
    #его вычисления
    eps = None
    while eps is None:
        eps = epsilon_check((input('Введите точность эпсилон: ')))
        if eps is None:
            print('Некорректный ввод')
    n = 1
    integral_1 = worst(end, start, n)
    integral_2 = worst(end, start, n* 2)
    while True:
        if abs(integral_1 - integral_2) < eps:
            print('Кол-во участков разбиения: ', n)
            print('Приближенное значение интеграла: ', f'{integral_1:.5g}')
            break
        n *= 2
        integral_1 = integral_2
        integral_2 = worst(end, start, n* 2)
        
else:
    print('Конец отрезка интегрирования должен быть больше начала')

