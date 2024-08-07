#Куликов Н.В. ИУ7-13Б
#Программа сортирует заданный массив методом Шелла,
#затем составляет таблицу замеров времени сортировки списков трёх различных
#размерностей и количества перестановок в каждом из них

from random import randint
import time

#Метод Шелла + счётчик кол-ва перестановок
def shell_sort(arr):
    n = len(arr)
    d = n // 2
    cnt = 0
    while d > 0:
        for i in range(d, n):
            j, t = i, arr[i]
            while j >= d and arr[j - d] > t:
                arr[j] = arr[j - d]
                cnt += 1
                j -= d
            arr[j] = t
        d //= 2
    return [arr, cnt]

#Проверка корректности ввода
def check(n):
    lst = list(n)
    if all(i in '0123456789' for i in lst) and lst[0] != '0':
        return True
    return False

#Секундомер
def timer(arr):
    start = time.time()
    shell_sort(arr)
    return time.time() - start

#Генератор сортированного списка
def sorted_list(n):
    return [int(i) for i in range(n)]

#Генератор сортированного в обратном порядке списка
def rsorted_list(n):
    return [int(i) for i in range(n, -1, -1)]

#Генератор случайного списка
def random_list(n):
    return [randint(-100, 100) for i in range(n)]

#Ввод массива пользователем и вывод отсортированного методом Шелла массива
try:
    a = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
    a = shell_sort(a)
except Exception:
    print('Некорректный ввод!')
else:
    print('Отсортированный массив: ', a[0])

    #Ввод размерностей с проверкой корректности ввода
    while True:
        n1 = input('Задайте размерность N1: ')
        n2 = input('Задайте размерность N2: ')
        n3 = input('Задайте размерность N3: ')
        if check(n1) and check(n2) and check(n3):
            n1, n2, n3 = int(n1), int(n2), int(n3)
            break
        print('Некорректный ввод!')

    #Вывод заголовка таблицы
    print('-' * 114)
    print(f'|{" ":28}|{"N1":^27}|{"N2":^27}|{"N3":^27}|')
    print('-' * 114)
    print(f'|{" ":28}|{"время":^12}|{"перестановки":^14}|{"время":^12}|{"перестановки":^14}|{"время":^12}|{"перестановки":^14}|')
    print('-' * 114)

    #Вывод значений для упорядоченного списка
    s = f'|{"Упорядоченный список":^28}'
    for n in [n1, n2, n3]:
        lst  = sorted_list(n)
        lst_t = lst
        k = shell_sort(lst_t)[1]
        s += f'|{timer(lst):^12.5g}|{k:^14}'
    s += '|'
    print(s)
    print('-' * 114)

    #Вывод значений для случайного списка
    s = f'|{"Случайный список":^28}'
    for n in [n1, n2, n3]:
        lst  = random_list(n)
        lst_t = lst
        k = shell_sort(lst_t)[1]
        s += f'|{timer(lst):^12.5g}|{k:^14}'
    s += '|'
    print(s)
    print('-' * 114)

    #Вывод значений для упорядоченного в обратном порядке списка
    s = f'|{"Упорядоченный в обр. порядке":^28}'
    for n in [n1, n2, n3]:
        lst  = rsorted_list(n)
        lst_t = lst
        k = shell_sort(lst_t)[1]
        s += f'|{timer(lst):^12.5g}|{k:^14}'
    s += '|'
    print(s)
    print('-' * 114)
