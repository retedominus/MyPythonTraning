import view
import data


def menu_initialisation():
    main_menu = view.menu_main()
    while True:
        view.print_menu('ГЛАВНОЕ МЕНЮ', main_menu)
        user_choice = view.get_user_choice(main_menu)
        if user_choice == 0:
            break

        if user_choice == 1:
            f_name = input("Введите имя файла (латиница): ")
            f_extension = view.menu_choose_file_format()
            data.create_pb(f_name + '.' + f_extension)

        if user_choice == 2:
            if type(data.is_phone_book_exist()) == dict:
                view.print_menu('Существующие телефонные книги', data.is_phone_book_exist())
                key = view.get_choice_pbook(data.is_phone_book_exist())
                dic = data.is_phone_book_exist()
                data.search_pb(dic[key])
            else:
                data.search_pb(data.is_phone_book_exist())

        if user_choice == 3:
            if type(data.is_phone_book_exist()) == dict:
                view.print_menu('Существующие телефонные книги', data.is_phone_book_exist())
                key = view.get_choice_pbook(data.is_phone_book_exist())
                dic = data.is_phone_book_exist()
                data.new_write_pb(dic[key])
            else:
                data.new_write_pb(data.is_phone_book_exist())

        if user_choice == 4:
            if type(data.is_phone_book_exist()) == dict:
                view.print_menu('Существующие телефонные книги', data.is_phone_book_exist())
                key = view.get_choice_pbook(data.is_phone_book_exist())
                dic = data.is_phone_book_exist()
                data.read_pb(dic[key])
            else:
                data.read_pb(data.is_phone_book_exist())

        if user_choice == 5:
            if type(data.is_phone_book_exist()) == dict:
                view.print_menu('Существующие телефонные книги', data.is_phone_book_exist())
                key = view.get_choice_pbook(data.is_phone_book_exist())
                dic = data.is_phone_book_exist()
                data.clear_pb(dic[key])
            else:
                data.clear_pb(data.is_phone_book_exist())

        if user_choice == 6:
            if type(data.is_phone_book_exist()) == dict:
                view.print_menu('Существующие телефонные книги', data.is_phone_book_exist())
                key = view.get_choice_pbook(data.is_phone_book_exist())
                dic = data.is_phone_book_exist()
                data.edit_rec(dic[key])
            else:
                data.edit_rec(data.is_phone_book_exist())
