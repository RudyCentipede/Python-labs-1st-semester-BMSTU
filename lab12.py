#Куликов Н.В. ИУ7-13Б
#Текстовый процессор
import math
#Отрисовка меню и вывод измененного текста
def menu(text):

    for i in text:
        print(i)
        
    print('\n\n')
    print('Ваши возможности (написать цифру):')
    print('1) Выровнять по левому краю')
    print('2) Выровнять по правому краю')
    print('3) Выровнять по ширине')
    print('4) Удаление всех вхождений слова')
    print('5) Замена одного слова другим')
    print('6) Сложение и вычитание целых чисел в тексте')
    print('7) Вывести самое короткое слово в предложении, в котором слов больше всего')
    print('8) Завершить программу')
    print('\n')
    while True:
        num = input('Выполнить: ')
        if all(i in '12345678' for i in num) and len(num) == 1:
            num = int(num)
            break
        print('Некорректный ввод!')
    if num == 1:
        left(text)
    elif num == 2:
        right(text)
    elif num == 3:
        width(text)
    elif num == 4:
        word = input('Введите слово: ')
        delete(text, word)
    elif num == 5:
        while True:
            word1 = input('Введите заменяемое слово: ')
            word2 = input('Введите слово, на которое меняется: ')
            if len(word1.split()) == 1 and len(word2.split()) == 1:
                break
            print('Некорректный ввод!')
        rep(text, word1, word2)
    elif num == 6:
        summary(text)
    elif num == 7:
        shortest(text)
    else:
        print('Программа успешно завершена!')

#Выравнивание по левому краю
def left(text):
    for i in range(len(text)):
        st = ''
        cnt = 0
        for j in text[i]:
            if j != ' ' or cnt > 0:
                st += j
                cnt += 1
        
        text[i] = st
    menu(text)

#Выравнивание по правому краю
def right(text):
    ma = 0
    for i in text:
        if len(i) > ma:
            ma = len(i)
    for i in range(len(text)):
        text[i] = text[i].rstrip()
        
    for i in range(len(text)):
        st = ''
        while len(text[i]) + len(st) < ma:
            st += ' '
        text[i] = st + text[i]
         
    menu(text)

#Выравнивание по ширине
def width(text):
    ma = 0
    for i in text:
        if len(i) > ma:
            ma = len(i)
    for i in range(len(text)):
        text[i] = text[i].strip()
        
    result = ""
    for line in text: 
        words = line.split(" ")
        if len(words) < 2:
            result += line.ljust(ma) + "\n"
        else:
            spaces = ma - len(line) + len(words) - 1

            n = math.floor(spaces / (len(words) - 1))
            k = spaces - n * (len(words) - 1)

            spaces =[n + 1] * k + [n] * (len(words) - k - 1)
            line = "".join(map(lambda w, s: w + " "*s, words, spaces)) + words[-1]
            result += line + "\n"

    text = result.split('\n')
    menu(text)

#Удаление всех вхождений слова
def delete(text, word):
    for i in range(len(text)):
        for j in range(len(text[i])):
            try:
                if text[i][j] == word[0]:
                    start = j
                    sl = ''
                    ki = i
                    kj = j
                    if j == 0 or text[i][j-1] == ' ':
                        while text[ki][kj].isalpha() and kj < len(text[i]):
                            sl += text[ki][kj]
                            kj += 1
                    if sl == word:
                        text[i] = text[i][:start] + text[i][kj:]
            except Exception:
                pass
                    
   
    menu(text)

#Замена всех вхождений слова на другое слово
def rep(text, word, word2):
    for i in range(len(text)):
        for j in range(len(text[i])):
            try:
                if text[i][j] == word[0]:
                    start = j
                    sl = ''
                    ki = i
                    kj = j
                    if j == 0 or text[i][j-1] == ' ':
                        while text[ki][kj].isalpha() and kj < len(text[i]):
                            sl += text[ki][kj]
                            kj += 1
                    if sl == word:
                        text[i] = text[i][:start] + word2 + text[i][kj:]
            except Exception:
                pass
    menu(text)

#Вычисление арифметических выражений внутри текста (+-)
def summary(text):
    for i in range(len(text)):
        st = ''
        tmp = text[i]
        for j in range(len(text[i])):
            if text[i][j] in '0123456789-+ ':
                if len(st) == 0:
                    start_index = j
                st += text[i][j]
                index = j
            elif len(st) > 0 and ('-' in st or '+' in st) and any(k in '0123456789' for k in st):
                st = st.replace(' ', '')
                if len(st) > 0:
                    numbers = []
                    symbols = ''
                    stt = ''
                    for k in st:
                        if k in '0123456789':
                            stt += k
                        else:
                            symbols += k
                            numbers.append(int(stt))
                            stt = ''
                    if stt != '':
                        numbers.append(int(stt))
                    if len(numbers) == len(symbols) + 1:    
                        result = numbers[0]
                        for k in range(len(symbols)):
                            if symbols[k] == '+':
                                result += numbers[k + 1]
                            else:
                                result -= numbers[k + 1]
                        st = ''
                        tmp = text[i][:start_index] + str(result) + text[i][index:]
                st = ''

        text[i] = tmp
    menu(text)

#Поиск и удаление самого короткого слова в предложении, в котором слов больше всего.
def shortest(text):
    mi_word_cur = ''
    mi_word_global = ''
    word = ''
    cu_len = 0
    ma_len = 0
    
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                word += text[i][j]
            elif text[i][j] in ' ,-+:;':
                cu_len += 1
                if len(mi_word_cur) > len(word) and word != '' or mi_word_cur == '':
                    mi_word_cur = word
                word = ''
            elif text[i][j] in '.!?':
                if cu_len > ma_len and mi_word_cur != '' and (len(mi_word_cur) < len(mi_word_global) or mi_word_global == ''):
                    ma_len = cu_len
                    mi_word_global = mi_word_cur
                word = ''
                cu_len = 0
                mi_word_cur = ''
            
    print('Cамое короткое слово в предложении, в котором слов больше всего:', mi_word_global)
    delete(text, mi_word_global)

#Отрисовка исходного текста
print('\n')
text = ['И все эти',
        '          160 - 10 миллионов людей,',
        'биллионы рыбин, ',
        '         триллионы насекомых,',
        '                       зверей,',
        '                            домашних животных,',
        '100 + 90 -9+ 1 сотни губерний,',
        '         со всем, что построилось,',
        '                                стоит,',
        '                                    живет в них,',
        'все, что может двигаться,',
        '      и все, что не движется,',
        '         все, что 12 + еле 11 двигалось,',
        '                      пресмыкаясь,',
        '                              ползая,',
        '                                плавая -',
        ' и Питер в питере, питер. Новые',
        '190 лавою все это,',
        '               лавою',
        'А гудело над местом,',
        '            где стояла когда-то Россия:',
        '                         - Это же ж не важно,',
        '                             чтоб торговать сахарином!',
        'В колокола клокотать чтоб — сердцу важно!',
        'Сегодня',
        '         в рай',
        '              Россию ринем',
        '200 за радужные закатов скважины!']
#Вызов меню
menu(text)
