#Куликов Н.В.
#Удалить все Положительные элементы целочисленного списка

print("Введите элементы списка через пробел, затем нажмите Enter")
a = [int(i) for i in input().split()]
count = 0                              #кол- во положительных элементов
if len(a) == 0:
    print("Нет элеиентов в списке!")
else:
    for i in range(len(a)):
        if a[i] > 0:
            count += 1
        else:
            a[i - count] = a[i]        #замена положительного элемента на отрицательный


    a = a[:len(a) - count]                 

    if len(a) == 0:
        print("Все элементы положительны")
    else:
        print(a)


    
    

