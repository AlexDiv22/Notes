def search_in_id():

    id = input("Введите ID для поиска заметки: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("id: " + id + "; ") in item:
                    print(item)
        else:
            print("Заметки не найдены")
        file.close()
def search_in_date():
    date = input("Введите дату и время для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("дата: " + date + "; ") in item:
                    print(item)
        else:
            print("Заметки не найдены")
        file.close()
def search_in_header():
    head = input("Введите заголовок для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("заголовок: " + head + "; ") in item:
                    print(item)
        else:
            print("Заметки не найдены")
        file.close()
def search_in_word():
    word = input("Введите ключевое слово для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if word in item:
                    print(item)
                else:
                    print("Не найдено")
                    return
        else:
            print("Заметки не найдены")
        file.close()


def search_in():
    print("Параметры поиска:\n 1 - ID \n 2 - Дата \n 3 - По заголовку\n 4 - По слову \n 0 - Выход \n")
    com = int(input())
    if com == 1:
        search_in_id()
    elif com == 2:
        search_in_date()
    elif com == 3:
        search_in_header()
    elif com == 4:
        search_in_word()
    elif com == 0:
        return
    print()