import Text

PHONEBOOK_FILE = 'phonebook.txt'  # Имя файла для сохранения телефонного справочника


def load_phonebook():
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


def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, 'w') as file:
        for name, contact in phonebook.items():
            surname = contact['surname']
            number = contact['number']
            comment = contact['comment']
            file.write(f"{name},{surname},{number},{comment}\n")


# Загрузка телефонного справочника при запуске программы
phonebook = load_phonebook()
