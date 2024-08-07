#Куликов Н.В. ИУ7-13
#4. Найти наиболее длинную непрерывную последовательность.
#Вариант 4  Убывающая последовательность простых чисел.


n = int(input("Введите кол-во элементов в списке: "))
a = [int(input()) for i in range(n)]

res = [a[0]]
answer = []
for i in range(len(a)-1):
    f = a[i]    
    s = a[i+1]  
    cf = 0      #кол-во делителей числа f
    cs = 0      #кол-во делителей числа s
    
    #Считаем кол-во делителей числа f
    for j in range(2, f):
        if f % j == 0:
            cf += 1
            
    #Считаем кол-во делителей числа s
    for j in range(2, s):
        if s % j == 0:
            cs += 1

    #Проверка, простые ли числа и убывают ли они
    if s < f and cf == 0 and cs == 0:
        res.append(s)
    else:
        if len(res) > len(answer):
            answer = res
        res = [s]

if len(answer) > 1:
    print(answer)
else:
    print("Нет убывающей последовательности простых чисел")
