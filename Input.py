def inputData():
    id = input("ID заметки: ")
    date = input("Дата и время создания заметки: ")
    header = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")

    return [id, date, header, text]