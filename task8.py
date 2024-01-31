import os


def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding = 'utf-8') as data:
            data.write("")

def add_new_user(name: str, phone: str, filename: str):
    with open(filename, 'r+t', encoding='utf-8') as wrtbl:
       lins_count = len(wrtbl.readlines())
       wrtbl.write(f"{lins_count + 1};{name};{phone}\n")


def read_all(filename: str) -> str:
    with open(filename, 'r', encoding = 'utf-8') as data:
        resolt = data.read()   
    return resolt


def search_user(data: str, filename: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Вхождений не найдено'


INFO_STRING = """ 
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копировать строку в файл
5 - выход
"""

DATASOURCE = 'phone.txt'

check_directory(DATASOURCE)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:        
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input('Введите ФИО пользователя:')
        phone = input('Введите номер телефона:')
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
    elif mode == 3:
        search = input('Введите строку для поиска: ')
        print(search_user(search, DATASOURCE))
    elif mode == 4:
        copyfile = input('Введите имя файла,куда копировать:')
        num_of_line = input('Введите номер строки справочника для копирования:')
        data=search_user(num_of_line+';',DATASOURCE)
        if data != 'Вхождений не найдено':
            check_directory(copyfile)
            data=data.split()
            add_new_user(data[1], data[2], copyfile)
        else:
            print('Такого номера строки не существует')
    elif mode == 5:
        print ('Bye!;-)')
        exit()
