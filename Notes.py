from Write import writeData
from Read import readData
from Search import searchData


while True:
    print("Выберите команду: \n 1 - создать заметку  2 - поиск заметки  3 - показать заметку  4 - редактировать  5 - удалить  0 - выход")
    com = int(input())
    if com == 1:
        writeData()
    elif com == 2:
        searchData()
    elif com == 3:
        readData()
    elif com == 4:
        print("режим редактирования не создан")
    elif com == 5:
        print("режим удаления не создан")
    elif com == 0:
        break