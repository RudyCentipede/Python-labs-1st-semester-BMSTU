#Куликов Н.В. ИУ7-13Б
#Программа, которая позволяет с помощью меню выполнить
#следующие действия:
#1. Выбрать файл для работы
#2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)
#3. Вывести содержимое базы данных
#4. Добавить запись в произвольное место базы данных
#5. Удалить произвольную запись из базы данных
#6. Поиск по одному полю
#7. Поиск по двум полям

import struct
import os

def menu(file):
    #Отрисовка меню
    print()
    print('Текущий файл: ', file)
    print('Ваши возможности:')
    print('1. Выбрать файл для работы',
          '2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)',
          '3. Вывести содержимое базы данных',
          '4. Добавить запись в произвольное место базы данных',
          '5. Удалить произвольную запись из базы данных',
          '6. Поиск по одному полю',
          '7. Поиск по двум полям',
          '8. Завершение программы', sep = '\n', end = '\n')
    
    #Выбор действия
    while True:
        n = input('Выберите действие (цифру): ')
        print()
        if n in '12345678' and n != '':
            n = int(n)
            break
        print('Некорректный ввод! Вы ввели не цифру.')

    if n == 1:
        file = input('Введите имя файла: ')
        menu(file)
    elif n == 2:
        if file == '':
            file = input('Введите имя файла: ')
        init(file)
    elif n == 3:
        if file == '':
            file = input('Введите имя файла: ')
        output(file)
    elif n == 4:
        if file == '':
            file = input('Введите имя файла: ')
        while True:
            line_index = input('Введите номер позиции: ')
            new_line = input('Введите артикул, название и код страны-производителя через пробел: ') 
            li = new_line.split()
            if len(li) == 3 and all(c.isdigit() for c in li[0]) and li[1].isalpha() and all(c.isdigit() for c in li[2]) and all(c in '1234567890' for c in line_index):
                line_index = int(line_index)
                break
            print('Некорректный ввод! Неправильно указаны атрибуты вставляемой строки и/или номер позиции не является числом')
        
        if line_index * 48 > os.path.getsize(file) or line_index < 1:
            print('Некорректный ввод! Номер позиции от 1 до <номер последнего элемента + 1>')
            menu(file)
        add(file, int(line_index), new_line)
    elif n == 5:
        if file == '':
            file = input('Введите имя файла: ')
        while True:
            num = input('Введите номер удаляемой записи: ')
            if num != '':
                break
            print('Некорректный ввод! Введите одно целое число.')
        num = int(num)
        if os.path.getsize(file) < num * 48 or num < 1:
            print('Записи с таким номером нет в файле')
            menu(file)
        else:
            remove(file, num)
    elif n == 6:
        if file == '':
            file = input('Введите имя файла: ')
        while True:
            field = input('Введите поле (Артикул, Название, Страна): ')
            element = input('Введите элемент: ')
            if any(i == field.lower() for i in ['артикул', 'название', 'страна']):
                break
            print('Некорректный ввод! Такого поля не существует.')
        find_by_one(file, field, element)
    elif n == 7:
        if file == '':
            file = input('Введите имя файла: ')
        while True:
            field1 = input('Введите 1 поле (Артикул, Название, Страна): ')
            field2 = input('Введите 2 поле (Артикул, Название, Страна): ')
            element1 = input('Введите 1 элемент: ')
            element2 = input('Введите 2 элемент: ')
            if any(i == field1.lower() for i in ['артикул', 'название', 'страна']) and any(i == field2.lower() for i in ['артикул', 'название', 'страна']):
                break
            print('Некорректный ввод! Такого поля не существует.')
        find_by_two(file, field1, field2, element1, element2)
    else:
        print('Программа успешно завершена!')


#Инициализировать базу данных
def init(direction):
    try:
        file = open(direction, 'wb')
    except Exception:
        print('Ошибка доступа к файлу')
    a  = []
    while True:
        s = input('Введите артикул, название и код страны-производителя через пробел: ')
        if s == '':
            break

        li = s.split()
        if len(li) == 3 and all(c.isdigit() for c in li[0]) and li[1].isalpha() and all(c.isdigit() for c in li[2]):
            a.append(s)
        else:
            print('Некорректный ввод данных!')

    for i in a:
        data = i.split()
        file.write(struct.pack(FORMAT, int(data[0]), data[1].encode(), int(data[2])))

    file.close()
    menu(direction)


#Вывести содержимое базы данных
def output(direction):
    try:
        file = open(direction, 'rb')
    except Exception:
        print('Такого файла не существует!')
        menu(direction)
    print('-' * 68)
    print(f'|{"Артикул":^12}|{"Название товара":^40}|{"Код страны":^12}|')
    print('-' * 68)
    while True:
        try:
            i = file.read(48)
            num, name, date = struct.unpack(FORMAT, i)
            name = name.decode().rstrip('\x00')
            print(f'|{num:^12}|{name:^40}|{date:^12}|')
        except Exception:
            break
    print('-' * 68)
    file.close()
    menu(direction)


#Поиск по одному полю
def find_by_one(direction, field, element):
    try:
        file = open(direction, 'rb')
    except Exception:
        print('Такого файла не существует!')
        menu(direction)
    
    ind = ['артикул', 'название', 'страна'].index(field.lower())

    print('-' * 68)
    print(f'|{"Артикул":^12}|{"Название товара":^40}|{"Код страны":^12}|')
    print('-' * 68)
    while True:
        try:
            i = file.read(48)
            num, name, date = struct.unpack(FORMAT, i)
            name = name.decode().rstrip('\x00')
            if str([num, name, date][ind]) == element:
                print(f'|{num:^12}|{name:^40}|{date:^12}|')
        except Exception:
            break

    print('-' * 68)
    file.close()
    menu(direction)


#Поиск по двум полям
def find_by_two(direction, field1, field2, element1, element2):
    print(direction, field1, field2, element1, element2)
    try:
        file = open(direction, 'rb')
    except Exception:
        print('Такого файла не существует!')
        menu(direction)
    
    ind_field1 = ['артикул', 'название', 'страна'].index(field1.lower())
    ind_field2 = ['артикул', 'название', 'страна'].index(field2.lower())
    
    print('-' * 68)
    print(f'|{"Артикул":^12}|{"Название товара":^40}|{"Код страны":^12}|')
    print('-' * 68)
    while True:
        try:
            i = file.read(48)
            num, name, date = struct.unpack(FORMAT, i)
            name = name.decode().rstrip('\x00')
            if str([num, name, date][ind_field1]) == element1:
                if str([num, name, date][ind_field2]) == element2:
                    print(f'|{num:^12}|{name:^40}|{date:^12}|')
        except Exception:
            break

    print('-' * 68)
    file.close()
    menu(direction)


#Добавление записи в произвольное место
def add(direction, line_index, new_line):
    LINE_SIZE = 48
    lines_count = os.path.getsize(direction) // 48
    with open(direction, 'r+b') as f:
        try:
            f.seek(-LINE_SIZE, os.SEEK_END)

            while lines_count > line_index - 1:
                prev_chunk = f.read(LINE_SIZE)
                f.write(prev_chunk)
                if line_index == 1:
                    if lines_count - line_index != 0:
                        f.seek(-LINE_SIZE * 3, os.SEEK_CUR)
                    else:
                        f.seek(0)
                else:
                    f.seek(-LINE_SIZE * 3, os.SEEK_CUR)
                lines_count -= 1
        except Exception:
            pass

        if lines_count == 0:
            f.seek(0)
        elif line_index != 1:
            f.seek(LINE_SIZE, os.SEEK_CUR)
        data = new_line.split()
        f.write(struct.pack(FORMAT, int(data[0]), data[1].encode(), int(data[2])))
    menu(direction)


#Удаление произвольной записи
def remove(direction, line_index):
    with open(direction, "r+b") as f:
        f.seek(48 * line_index)
        while True:
            line = f.read(48)
            if not line:
                break
            f.seek(-48 * 2, os.SEEK_CUR)
            f.write(line)
            f.seek(48, os.SEEK_CUR)

        f.truncate(os.path.getsize(direction) - 48)
    menu(direction)


FORMAT = 'i 40s i'
menu('')
