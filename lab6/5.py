#Куликов Н.В. ИУ7-13
#5. Поменять местами элементы с характеристиками по варианту.
#Вариант 7  Последний нулевой и максимальный отрицательный.


n = int(input("Введите кол-во элементов в списке: "))
a = [int(input()) for i in range(n)]

if a.count(0) == 0:
    print("Нет нуля, замена невозможна")
else:
    
    ind_0 = len(a) - 1 - a[::-1].index(0)   #индекс последнего нулевого элемента
    ind_ma = 0                              #индекс максимального отрицательного элемента
    ma = min(a)

    if ma >= 0:
        print("Нет отрицательных элементов, замена невозможна")
    else:
        #Находим максимальный отрицательный элемент
        for i in a:
            if i < 0 and i > ma:
                ma = i
        ind_ma = a.index(ma)

        #Меняем местами элементы
        t = a[ind_0]
        a[ind_0] = a[ind_ma]
        a[ind_ma] = t

        print(a)
            
