#Куликов Н.В. ИУ7-13
#Замена всех заглавных гласных английских букв на строчные в списке строк

print("Введите элементы списка через пробел, затем нажмите Enter")
a = [i for i in input().split()]

if len(a) == 0:
    print('Введен пустой список')
else:
    upper = 'AEYUIO'         #английские заглавные гласные буквы
    lower = 'aeyuio'         #английские строчные гласные буквы
    for i in range(len(a)):
        s = ''              #в
        for k in range(len(a[i])):
            #если буква из строки a[i] английская заглавная гласная
            #
            if a[i][k] in upper:
                s += lower[upper.index(a[i][k])]
            else:
                s += a[i][k]
        a[i] = s

    print(a)
