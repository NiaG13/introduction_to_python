import view
import model
import text

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(view.key_name(new)))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                if result != {}:
                    choice_contact = view.change_index(text.choice_changeble_contact)
                    if model.check_contact(choice_contact, result):
                        contact_changes = view.add_change_contact()
                        changed_contact = model.changed_contact(choice_contact, contact_changes)
                        view.print_message(text.successful_change(view.key_name(changed_contact)))
                    else:
                        view.print_message(text.error_choice(choice_contact))
            case 7:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                if result != {}:
                    choice_contact = view.change_index(text.choice_deleted_contact)
                    if model.check_contact(choice_contact, result):
                        delet_contact = model.delet_contact(choice_contact)
                        view.print_message(text.successful_delet(view.key_name(delet_contact)))
                    else:
                        view.print_message(text.error_choice(choice_contact))
            case 8:
                view.print_message(text.end_message)
                return
