# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.
from os import path
from itertools import groupby, starmap


def rle_encoding(source_file='text_words.txt', rec_file='for_code_words.txt'):
    if path.exists(source_file) and path.exists(rec_file):
        with open(source_file) as f_1, open(rec_file, 'a') as f_2:
            for i in f_1:
                f_2.write("".join([f'{len(list(value))}{char}' for char, value in groupby(i)]))
    else:  # функцией groupby  в char вытаскиваем ключ - первая буква и в value  список букв
        print("Error, file doesn't exist in the system!")


def rle_decoding(file_name='for_code_words.txt'):
    if path.exists(file_name):
        with open(file_name) as file:  # открываем на чтение без 'r'
            num = ""  # временное хранилище для цифр (чтобы понять кол-во, если цифра более 1 знака)
            for i in file:  # вытягиваем циклом строки из файла
                word_nums = []
                for j in i.strip():  # чистим
                    if j.isdigit():
                        num += j  # цифры складываем
                    else:
                        word_nums.append([int(num), j])
                        # формируем подсписок содержащий цифру и букву
                        num = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
                # применяем к word_nums функцию перемножения буква на цифру
                num = ""  # необходимо обнулить хранилище, т.к. остается единица непечатаемого символа переноса
    else:
        print("Error, the file doesn't exist in the system!")


rle_encoding(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
rle_decoding(input("Enter the file name to decode: "))
