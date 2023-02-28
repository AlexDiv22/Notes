from Write import writeData
from Read import readData
from Search import searchData
from Delete import deleteData
from Edit import editData
2

while True:
    print("Выберите команду: \n 1 - создать заметку  2 - поиск заметки  3 - показать заметку  4 - редактировать  5 - удалить  0 - выход")
    com = input()
    if com == '1':
        writeData()
    elif com == '2':
        searchData()
    elif com == '3':
        readData()
    elif com == '4':
        editData()
    elif com == '5':
        deleteData()
    elif com == '0':
        break
    else:
        print("Введите цифру от 0 до 5")