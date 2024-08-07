#Куликов Н.В. ИУ7-13Б
#После каждого чётного числа добавить его удвоенное значение (допускается два прохода по файлу).
import os
import struct

def process_file(filename):
    #Запись чисел в файл
    with open(filename, 'wb') as f:
        numbers = [1, -2, -3, 4, 5]
        for num in numbers:
            f.write(struct.pack('l', num))
            
    #Добавление удвоенных значений после четных чисел
    double_even_numbers(filename)

    #Вывод измененного содержимого файла
    with open(filename, 'rb') as f:
        while True:
            num_bytes = f.read(4)
            if not num_bytes:
                break
            num = struct.unpack('l', num_bytes)[0]
            print(num)



def double_even_numbers(path):
    LINE_SIZE = 4
    nums_count = os.path.getsize(path) // 4
    count = 0
    with open(path, "r+b") as f:
        for i in range(nums_count):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack('l', num_bin)[0]
            if num % 2 == 0:
                count += 1
        for i in range(count):
            f.seek(0, os.SEEK_END)
            f.write(struct.pack('l', 0))

    with open(path, "r+b") as f:
        end_ind = nums_count - 1 + count
        for i in range(nums_count - 1, -1, -1):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack('l', num_bin)[0]
            if num % 2 == 0:
                f.seek(LINE_SIZE * end_ind)
                f.write(struct.pack('l', num * 2))
                f.seek(LINE_SIZE * (end_ind - 1))
                f.write(struct.pack('l', num))
                end_ind -= 2
            else:
                f.seek(LINE_SIZE * end_ind)
                f.write(struct.pack('l', num))
                end_ind -= 1





process_file('test2.bin')
