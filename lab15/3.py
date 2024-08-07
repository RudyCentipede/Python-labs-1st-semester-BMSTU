#Куликов Н.В. ИУ7-13Б
#Сортировка методом вставок с бинарным поиском

import os
import struct


def process_file(filename):
    #Запись чисел в файл
    with open(filename, 'wb') as f:
        numbers = [1, 4, 3, 2, 6, 5]
        for num in numbers:
            f.write(struct.pack('l', num)) 


    #Сортировка
    sort(filename)


    #Вывод измененного содержимого файла
    with open(filename, 'rb') as f:
        while True:
            num_bytes = f.read(4)
            if not num_bytes:
                break
            num = struct.unpack('l', num_bytes)[0]
            print(num)


def binary_search(path, item, low, high):
    LINE_SIZE = 4
    with open(path, "r+b") as f:
        while low <= high:
            mid = low + (high - low) // 2
            f.seek(LINE_SIZE * mid)
            mid_num_bin = f.read(LINE_SIZE)
            mid_num = struct.unpack('l', mid_num_bin)[0]
            if item == mid_num:
                return mid + 1
            elif item > mid_num:
                low = mid + 1
            else:
                high = mid - 1
    return low


def sort(path):
    LINE_SIZE = 4
    nums_count = os.path.getsize(path) // 4
    with open(path, "r+b") as f:
        for i in range(nums_count):
            j = i - 1
            # selected = data[i]
            f.seek(LINE_SIZE * i)
            selected_bin = f.read(LINE_SIZE)
            selected = struct.unpack('l', selected_bin)[0]

            insert_loc = binary_search(path, selected, 0, j)

            while j >= insert_loc:
                f.seek(LINE_SIZE * j)
                num_bin = f.read(LINE_SIZE)
                f.seek(LINE_SIZE * (j + 1))
                f.write(num_bin)
                j -= 1
            f.seek(LINE_SIZE * (j + 1))
            f.write(selected_bin)


process_file('test.bin')


