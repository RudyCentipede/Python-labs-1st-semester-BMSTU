#Куликов Н.В. ИУ7-13 75 вариант
#Написать программу, которая вычисляет сумму ряда с точностью до eps и выводит таблицу промежуточных значений переменных и сумм

x = float(input("Введите значение x: "))
eps = float(input("Введите точность: "))
h = float(input("Введите шаг печати: "))
steps = float(input("Введите кол-во итераций: "))

su = 1
i = 1
result = False

#Вывод заголовка таблицы
print('-' * 46)
print(f'| {"№ итерации":^12} | {"t":^12} | {"s":^12} |')
print('-' * 46)

#Вывод промежуточных значений t  и s
while i <= steps:
    t = ((-1) ** i * ((i + 1) * (i + 2)) * x ** i) / 2
    su += t
    #Проверка, достигли ли мы заданной точности эпсилон
    if abs(t) < eps:
        print('-' * 46)
        print("Сумма бесконечного ряда - {:g}".format(su), 'вычислена за {:g}'.format(i), 'итераций')
        result = True
        break
    print(f'| {i:<12g} | {t:^12.5g} | {su:^12.5g} |')
    i += h

#В случае, если заданная точность не достигнута
if result == False:
    print('-' * 46)
    print('За указанное число итераций необходимой точности достичь не удалось')
