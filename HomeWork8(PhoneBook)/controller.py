import Text
import View
import Modul


# Главное меню
def start():
    while True:
        choice = View.main_menu()
        if choice == 1:
            View.add_contact(Modul.phonebook)
        elif choice == 2:
            View.remove_contact(Modul.phonebook)
        elif choice == 3:
            View.search_contact()
        elif choice == 4:
            View.print_message(Text.pb_all_contact)
            View.show_all_contacts(Modul.phonebook)
        elif choice == 5:
            View.edit_contact(Modul.phonebook)
        elif choice == 6:
            print(Text.main_menu_end)
            break
        else:
            print(Text.main_menu_error)



