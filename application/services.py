from .data_pack.data import directories, documents


def add_new_shelf():
    """
    Функция спросит номер новой полки и добавит ее в перечень.
    shelf_number: пользовательский ввод - номер новой полки.
    return: результат выполнения операции.
    """
    print('Создаю новую полку\n')
    shelf_number = input('Введите номер новой полки: ')
    if str(shelf_number) not in directories:
        shelf_number = str(shelf_number)
        directories[shelf_number] = []
        return f'Полка с номером "{shelf_number}" успешно добавлена!\n{directories}\n'

    else:
        return f'Полка с номером "{shelf_number}" уже существует!\n{directories}\n'


def add_new_doc():
    """
    Функция, которая добавит новый документ в каталог и в перечень полок,
    спросив его номер, тип, имя владельца и номер полки, на которой он будет храниться.
    type_doc: пользовательский ввод - тип документа.
    doc_number: пользовательский ввод - номер документа.
    name: пользовательский ввод - имя владельца документа.
    shelf_number: пользовательский ввод - номер полки, для хранения документа.
    """
    type_doc = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    name = input('Введите имя владельца: ')
    shelf_number = input('Введите номер полки: ')
    if 1 <= int(shelf_number) <= len(directories):
        documents.append({'type': type_doc, 'number': doc_number, 'name': name})
        for key, value in directories.items():
            if str(shelf_number) in key:
                directories[key] = value + [doc_number]
                return f'{type_doc} с номером "{doc_number}" успешно добавлен на полку №"{shelf_number}"\n' \
                       f'{directories}\n'
    else:
        return f'Такой полки не существует!\n{directories}\n'


def move_doc():
    """
    Функция спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    doc_number: пользовательский ввод - номер документа.
    shelf_number: пользовательский ввод - номер полки, куда переместить документ.
    return: результат выполнения операции.
    """
    doc_number = input('Введите номер документа: ')
    shelf_number = input('Введите номер полки: ')
    for document in directories.values():
        if doc_number in document:
            if 1 <= int(shelf_number) <= len(directories):
                document.remove(doc_number)
                for key, value in directories.items():
                    if str(shelf_number) in key:
                        directories[key] = value + [doc_number]
                        return (f'Документ с номером "{doc_number}" успешно перемещен!\n'
                                f'{directories}\n')
            else:
                return f'Такой полки не существует!\n{directories}\n'
    return f'Документа с номером "{doc_number}" в базе нет!\n'


def del_doc():
    """
    Функция, спросит номер документа и удалит его из каталога и из перечня полок.
    doc_number: пользовательский ввод - номер документа.
    return: результат выполнения операции.
    """
    doc_number = input('Введите номер документа: ')
    for value in directories.values():
        if doc_number in value:
            value.remove(doc_number)
    for document in documents:
        if document.get('number') == doc_number:
            documents.remove(document)
            return f'Документ с номером "{doc_number}" успешно удален!\n{directories}\n'
    return f'Документа с номером "{doc_number}" в базе нет!\n'


def return_name():
    """
    Функция, по номеру документа, возвращает имя владельца.
    doc_number: пользовательский ввод - номер документа.
    return: имя владельца документа (если документ с таким номером есть в базе).
    """
    print('Поиск владельца по номеру документа.\n')
    doc_number = input('Введите номер документа: ')
    for document in documents:
        if document.get('number') == doc_number:
            return f'Владелец документа с номером "{doc_number}" - "{document["name"]}"\n'
    return f'Документа с номером "{doc_number}" в базе нет!\n'


def return_number_shelf():
    """
    Функция, по номеру документа, возвращает номер полки, на которой он находится.
    doc_number: пользовательский ввод - номер документа.
    return: номер полки на которой находится документ (если документ с таким номером есть в базе).
    """
    print('Поиск полки, на которой хранится документ.\n')
    doc_number = input('Введите номер документа: ')
    for key, value in directories.items():
        if doc_number in value:
            return f'Документ с номером "{doc_number}" хранится на полке №"{key}"\n'
    return f'Документа с номером "{doc_number}" в базе нет!\n'


def all_docs_in_base():
    """Функция выводит информацию по всем документам, имеющимся в базе."""
    print("Все документы имеющиеся в базе:\n")
    if len(documents) < 1:
        print('В базе нет документов!')
    for value in documents:
        print(f'{value["type"]} "{value["number"]}" "{value["name"]}"')
    print()


def show_commands():
    """Выводит список всех доступных команд"""
    commands = [
        'l – выведет список всех документов',
        'p – по номеру документа выведет имя человека, которому он принадлежит',
        's – по номеру документа выведет номер полки, на которой он находится',
        'as – добавит в перечень новую полку по номеру',
        'a – добавит новый документ в каталог и в перечень полок',
        'd – по номеру документа удалит его из каталога и из перечня попок',
        'm – по номеру документа и целевой полки переместит его с текущей полки на целевую',
        'q - для завершения сеанса'
    ]
    print("Cписок всех доступных команд: \n")
    print('\n'.join(commands), '\n')


def main():
    commands = {
        'h': show_commands,
        'p': lambda: print(return_name()),
        's': lambda: print(return_number_shelf()),
        'l': all_docs_in_base,
        'as': lambda: print(add_new_shelf()),
        'a': lambda: print(add_new_doc()),
        'd': lambda: print(del_doc()),
        'm': lambda: print(move_doc()),
        'q': 'Выход из программы',
    }

    print("Мое делопроизводство v1.0")
    print("Введите 'h' что бы получить список всех доступных команд\n")

    while True:
        command = input('Введите команду: ')
        if command in commands:
            if command == 'q':
                print('Сеанс завершен. Хорошего дня!')
                break
            else:
                commands[command]()
        else:
            print('Такой команды нет. Выберите из доступных.')
            print('Введите "h" что бы получить список всех доступных команд')
