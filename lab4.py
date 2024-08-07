#Куликов Н.В. ИУ7-13
#14 вариант
#Программа выводит таблицу значений ф-ций: P = 0.471 * e ** (-a) * cos(pi * a ** 2) и R = 0.21 - 2.52 * a + a ** 3,
#строит график ф-ции R, запрашивая у юзера кол-во засечек на оси у
#найти максимальное значение ф-ции R и а в котором оно достигается

from math import *

a0 = float(input("Введите начальное значение: "))
h = float(input("Введите шаг: "))
an = float(input("Введите конечное значение: "))

#Вывод заголовка таблицы
print("-" * 46)
print(f'| {"a":^12} | {"P":^12} | {"R":^12} |')
print("-" * 46)

eps = 1e-8
steps = int(round((an-a0)/h))  #кол-во значений, подставляемых в ф-цию

a = a0

r_max = 0
a_max = 0
r_min = float('+inf')

#Вывод таблицы значений ф-ций
for _ in range(steps+1):
    P = 0.471 * e ** (-a) * cos(pi * a ** 2)
    R = 0.21 - 2.52 * a + a ** 3
    if R > r_max:
        r_max = R
        a_max = a
    r_min = min(r_min, R)
    if round(an, 5) >= round(a, 5):
        print(f'| {a:^12.5g} | {P:^12.5g} | {R:^12.5g} |')
    a += h
    
print("-" * 46, end='\n\n')

zas = int(input("Введите кол-во засечек (целое число от 4 до 8 включительно): "))

width = 100                              #ширина графика
znach = (r_max - r_min) / (zas - 1)      #число на оси у
m = width / (r_max - r_min)              #масштаб
rast = (width - zas * 12) / (zas - 1)    #кол-во пробелов
y = ' ' * 13                             #ось у
r = r_min


#Формирование оси у
for i in range(zas):
    y += f'{r:<12.5g}' + ' ' * int(rast)
    r += znach

print(y)

nol = 14 + (int(m * (-r_min)) - 1)
a = a0

#Вывод графика ф-ции R
for _ in range(steps+1):
    r = 0.21 - 2.52 * a + a ** 3

    before = (int(m * (r - r_min)) - 1)            #кол-во пробелов до *
    after = (width - 11 - int(m * (r - r_min)) - 1)  #кол-во пробелов после *

    if r_min <= 0 <= r_max:
        ss = f'{a:<12.5g}|' + ' ' * before + '*' + ' ' * after
        if ss[nol] != '*':
            ss = ss[:nol] + '|' + ss[nol + 1:]
        print(ss)
    else:
        print(f'{a:<12.5g}|' + ' ' * before + '*' + ' ' * after)
    
    a += h

print("Максимальное значение R: {:g}".format(r_max))
print("Значение а, при котором R - максимально: {:g}".format(a_max))
