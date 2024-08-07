#Куликов Н.В. ИУ7-13Б
#Удалить все Положительные элементы за один проход по файлу

import os
import struct

def process_file(filename):
    #Запись чисел в файл
    with open(filename, 'wb') as f:
        numbers = [1, -2, 3, -4, 5]
        for num in numbers:
            f.write(struct.pack('l', num)) 


    #Удаление положительных элементов
    LINE_SIZE = 4
    nums_count = os.path.getsize(filename) // 4
    count = 0
    with open(filename, "r+b") as f:
        for i in range(nums_count):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack('l', num_bin)[0]
            if num > 0:
                count += 1
            else:
                f.seek(LINE_SIZE * (i - count))
                f.write(num_bin)
        f.truncate(os.path.getsize(filename) - LINE_SIZE * count)


    #Вывод измененного содержимого файла
    with open(filename, 'rb') as f:
        while True:
            num_bytes = f.read(4)
            if not num_bytes:
                break
            num = struct.unpack('l', num_bytes)[0]
            print(num)

process_file('test.bin')


