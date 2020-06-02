# Каталог документов хранится в следующем виде:
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def search_people(numbers):
    for doc_numbers in documents:
        if doc_numbers["number"] == numbers:
            print(doc_numbers["name"])
            break
    else:
        print('Документа с таким номером нет в каталоге.')


def print_list():
    for persons in documents:
        print(persons['type'], '"' + persons['number'] + '"', '"' + persons['name'] + '"')


def search_shelf(numbers):
    break_marker = False
    for shelf_directories in directories.items():
        for doc_numbers in shelf_directories[1]:
            if doc_numbers == numbers:
                print('Документ находится на полке №', shelf_directories[0])
                break_marker = True
                break
        if break_marker == True:
            break
    else:
        print('Документа с таким номером нет в каталоге.')


def add_document(params_type, number, name, directories_number):
    if int(directories_number) == 1 or int(directories_number) == 2 or int(directories_number) == 3:
        documents.append({"type": params_type, "number": number, "name": name})
        directories[directories_number].append(number)
        print('Документ успешно добавлен.')
    else:
        print('Вы ввели неверный номер полки. Запись не произведена.')


def get_names(documents):
    names = []
    for document in documents:
        try:
            names.append(document['name'])
        except (Exception, KeyError) as e:
            print(f'Найден документ без поля {e}')
    names = set(names)
    print(f'Список владельцев документов: {names}')


while True:
    command = input('\n \
  Выберите команду: p, s, l, n или a. \n \
  Справка по командам: help.\n \
  Для выхода из программы: q. \n \
  Введите вашу команду: ').lower()
    if command == 'p':
        search_people(input('\nВведите номер документа: '))
    elif command == 'l':
        print_list()
    elif command == 's':
        search_shelf(input('\nВведите номер документа: '))
    elif command == 'a':
        add_document(input('\nВведите тип документа: '), input('Введите номер документа: '),
                     input('Введите имя и фамилию владельца: ').capitalize(), input('Введите номер полки 1, 2 или 3: '))
    elif command == 'n':
        get_names(documents)
    elif command == 'q':
        break
    elif command == 'help':
        print('\n \
    p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n \
    s – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n \
    l – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n \
    n - команда, которая выведет имена владельцев документов;\n \
    a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    else:
        print('Неверная команда, повторите ввод или вызовите справку.')