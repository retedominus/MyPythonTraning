import csv
import glob
from os import path


def create_pb(f_name: str):
    if not path.exists(f_name):
        load_data = [input("Введите имя контакта: \n").lower().capitalize(), input("Введите номер телефона: \n")]
        with open(f_name, 'a', encoding="utf-8") as file:
            if 'csv' in f_name:
                writer = csv.writer(file)
                writer.writerow(load_data)
            else:
                file.write(f'{", ".join(load_data)}\n')
        print("\nФайл телефонной книги создан.")
    else:
        print('\nТакой файл уже существует. Хотите добавить новую запись?')


def is_phone_book_exist():
    f_list = glob.glob('*.csv') + glob.glob('*.txt')
    if len(f_list) > 1:
        f_dict = dict(enumerate(f_list, 1))
        return f_dict
    else:
        f_list = "".join(f_list)
        return f_list


def new_write_pb(file_name: str):
    if path.exists(file_name):
        pers_name = input("Введите имя контакта: ").lower().capitalize()
        ph_num = input("Введите номер телефона: ")
        data = [pers_name, ph_num]
        with open(file_name, 'a', encoding="utf-8") as file:
            if 'csv' in file_name:
                writer = csv.writer(file)
                writer.writerow(data)
            else:
                file.write(f'{", ".join(data)}\n')
        print("Запись добавлена.")
    else:
        print("\nТелефонная книга не найдена. Создайте новую.")


def edit_rec(file_name):
    name = input('Введите имя контакта:\n').lower().capitalize()
    temp_list = []
    match_found = 0
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            temp_list.append(row)
            if name in row:
                match_found += 1
                temp_list.pop()
                temp_list.append(ask_edit_return(row))
    if match_found > 0:
        with open(file_name, 'w') as f_edit:
            writer = csv.writer(f_edit)
            writer.writerows(temp_list)
    else:
        print("\nНет такой записи\n")


def ask_edit_return(r_row: list):
    answer = int(input("\nЧто изменить:\n1 - Имя\n2 - Номер телефона\n3 - Выход\n"))
    match answer:
        case 1:
            r_row.pop(answer - 1)
            r_row.insert(answer - 1, input("\nВведите новое имя контакта: \n").lower().capitalize())
            return r_row
        case 2:
            r_row.pop(answer - 1)
            r_row.insert(answer - 1, input("\nВведите новый номер телефона: \n"))
            return r_row
        case 3:
            return r_row


def read_pb(file_name):
    if path.exists(file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            line_count = 0
            for row in reader:
                print(f'Имя: {row[0]}   Телефон: {row[1]}')
                line_count += 1
            print(f'\nВсего в телефонной книге {line_count} записей')
    else:
        print('\nТелефонная книга не найдена. Создайте новую.')


def clear_pb(file_name):
    if path.exists(file_name):
        answer = input('\nВы уверены, что хотите удалить все записи? 1 - да, 9 - нет, выход\n')
        if not answer.isdigit() or int(answer) != 1 and int(answer) != 9:
            print('\nВведены некорректные данные. Попробуйте снова.')
            clear_pb(file_name)
        elif answer.isdigit() and int(answer) == 1:
            with open(file_name, 'w') as file:
                file.write('')
            print('\nВсе записи удалены.')
        else:
            print('\nУдаление всех данных отменено.')
    else:
        print('\nТелефонная книга не найдена. Создайте новую.')


def search_pb(file_name):
    if path.exists(file_name):
        value = input('Введите имя контакта: \n').lower().capitalize()
        print(value)
        counter = 0
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if value in row:
                    counter += 1
                    print(f'\nЗвоните контакту {row[0]} по телефону: {row[1]}')
            if not counter:
                print('\nТакая запись не найдена')
    else:
        print('\nТелефонная книга не найдена. Создайте новую.')
