PHONEBOOK_FILE = 'phonebook.txt'  # Имя файла для сохранения телефонного справочника


def load_phonebook():
    try:
        with open(PHONEBOOK_FILE, 'r') as file:
            phonebook = {}
            for line in file:
                name, surname, number, comment = line.strip().split(',')
                phonebook[name] = {
                    'surname': surname,
                    'number': number,
                    'comment': comment
                }
            return phonebook
    except FileNotFoundError:
        return {}


def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, 'w') as file:
        for name, contact in phonebook.items():
            surname = contact['surname']
            number = contact['number']
            comment = contact['comment']
            file.write(f"{name},{surname},{number},{comment}\n")


def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    phonebook[name] = {
        'surname': surname,
        'number': number,
        'comment': comment
    }
    save_phonebook(phonebook)
    print("Контакт добавлен")


def remove_contact():
    name = input("Введите имя контакта для удаления: ")
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print("Контакт удален")
    else:
        print("Контакт не найден")


def search_contact():
    name = input("Введите имя контакта для поиска: ")
    if name in phonebook:
        contact = phonebook[name]
        print(
            f"Имя: {name}, Фамилия: {contact['surname']}, Номер: {contact['number']}, Комментарий: {contact['comment']}")
    else:
        print("Контакт не найден")


def show_all_contacts():
    if phonebook:
        print("Телефонный справочник:")
        for name, contact in phonebook.items():
            print(
                f"Имя: {name}, Фамилия: {contact['surname']}, Номер: {contact['number']}, Комментарий: {contact['comment']}")
    else:
        print("Телефонный справочник пуст")


def edit_contact():
    name = input("Введите имя контакта для изменения: ")
    if name in phonebook:
        contact = phonebook[name]
        print(f"Редактирование контакта: {name}")
        print(f"Текущая фамилия: {contact['surname']}")
        new_surname = input("Введите новую фамилию (оставьте пустым для сохранения текущей): ")
        if new_surname:
            contact['surname'] = new_surname

        print(f"Текущий номер: {contact['number']}")
        new_number = input("Введите новый номер (оставьте пустым для сохранения текущего): ")
        if new_number:
            contact['number'] = new_number

        print(f"Текущий комментарий: {contact['comment']}")
        new_comment = input("Введите новый комментарий (оставьте пустым для сохранения текущего): ")
        if new_comment:
            contact['comment'] = new_comment

        save_phonebook(phonebook)
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")


# Загрузка телефонного справочника при запуске программы
phonebook = load_phonebook()

# Главное меню
while True:
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Поиск контакта")
    print("4. Показать все контакты")
    print("5. Изменить контакт")
    print("6. Выйти")
    choice = input("Выберите действие (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        show_all_contacts()
    elif choice == '5':
        edit_contact()
    elif choice == '6':
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

print("Программа завершена.")
