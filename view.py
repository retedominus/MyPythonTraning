
def menu_choose_file_format():
    answer = int(input("Выберите формат файла:\n1: CSV\n2: TXT\n0: ВЫХОД\n"))
    match answer:
        case 1:
            return "csv"
        case 2:
            return "txt"
        case 0:
            return 0
        case _:
            print('Вы указали не верный пункт меню')


def menu_main():
    menu = {1: 'Создать новую телефонную книгу', 2: 'Поиск по телефонной книге',
            3: 'Добавить запись в телефонную книгу', 4: 'Вывести телефонную книгу в консоль',
            5: 'Очистить телефонную книгу', 6: 'Редактировать запись', 0: 'ВЫХОД'}
    return menu


def print_menu(menu_title, menu_data):
    print(f'\n-----{menu_title}-----')
    for key_menu, title_menu in menu_data.items():
        print(key_menu, '-', title_menu)


def get_user_choice(menu):
    answer = input('\nВыберите пункт меню: \n')
    while not answer.isdigit() or int(answer) not in menu.keys():
        print("Вы указали неверный пункт меню. Попробуйте снова.")
        answer = input('\nВыберите пункт меню: \n')
    return int(answer)


def get_choice_pbook(menu):
    answer = input('\nВыберите телефонную книгу\n')
    while not answer.isdigit() or int(answer) not in menu.keys():
        print("\nОшибка ввода. Попробуйте снова.")
        answer = input('\nВыберите телефонную книгу\n')
    return int(answer)


