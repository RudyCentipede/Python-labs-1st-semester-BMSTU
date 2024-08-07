#Куликов Н.В. ИУ7-13
#3. Найти значение K-го экстремума в списке.

n = int(input("Введите кол-во элементов в списке: "))
a = [int(input()) for i in range(n)]
k = int(input("Введите K: "))

extr = [] 
#Находим эстремумы и добавляем в extr
for i in range(1, len(a)- 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1] or a[i] < a[i - 1] and a[i] < a[i + 1]:
        extr.append(a[i])
        
#Выводим К-тый экстремум
if len(extr) != 0:
    if len(extr) >= k:
        print(extr[k-1])
    else:
        print("В данном списке нет экстремума под таким номером")
else:
    print("А вот нету тут экстремумов, понял?")
    
