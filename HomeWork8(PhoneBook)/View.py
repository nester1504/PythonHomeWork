import Text
import Modul


def main_menu() -> int:
    print(Text.main_menu)
    while True:
        choice = input(Text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def show_all_contacts(phonebook):
    if phonebook:
        print(Text.pb_all_contact_table)
        print(Text.pb_all_contact_divider)
        for name, contact in phonebook.items():
            name = name.ljust(12)
            surname = contact['surname'].ljust(10)
            number = contact['number'].ljust(12)
            comment = contact['comment'].ljust(17)
            print(f"|  {name}  |  {surname}  |  {number}  |  {comment}  |")
        print(Text.pb_all_contact_divider)
    else:
        print(Text.pb_empty)


def add_contact(phonebook):
    new_contact = {}
    fields = ['name', 'surname', 'number', 'comment']
    for field in fields:
        user_input = input(Text.new_contact[field])
        new_contact[field] = user_input

    phonebook[new_contact['name']] = {
        'surname': new_contact['surname'],
        'number': new_contact['number'],
        'comment': new_contact['comment']
    }
    Modul.save_phonebook(phonebook)
    print(Text.add_new_contact)


def remove_contact(phonebook):
    name = input(Text.input_del_contact)
    if name in phonebook:
        del phonebook[name]
        Modul.save_phonebook(phonebook)
        print(Text.del_contact)
    else:
        print(Text.no_contact)


def search_contact(phonebook):
    name = input(Text.search_contact)
    if name in phonebook:
        contact = phonebook[name]
        print(
            f"Имя: {name}, Фамилия: {contact['surname']}, Номер: {contact['number']}, Комментарий: {contact['comment']}")
    else:
        print(Text.no_contact)


def edit_contact(phonebook):
    name = input(Text.new_name)
    if name in phonebook:
        print(f"Редактирование контакта: {name}")
        print(f"Текущее имя: {name}")
        new_name = input(Text.new_name)
        if new_name:
            phonebook[new_name] = phonebook.pop(name)  # Замена ключа в словаре
            name = new_name
        contact = phonebook[name]
        print(f"Текущая фамилия: {contact['surname']}")
        new_surname = input(Text.new_surname)
        if new_surname:
            contact['surname'] = new_surname

        print(f"Текущий номер: {contact['number']}")
        new_number = input(Text.new_number)
        if new_number:
            contact['number'] = new_number

        print(f"Текущий комментарий: {contact['comment']}")
        new_comment = input(Text.new_comment)
        if new_comment:
            contact['comment'] = new_comment

        Modul.save_phonebook(phonebook)
        print(Text.edit_contact_good)
    else:
        print(Text.no_contact)
