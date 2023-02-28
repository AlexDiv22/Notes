def deleteData():
    print("Заметку можно удалить по номеру строки")
    with open("data.txt") as file:
        id_del = int(input())
        id_note = file.readlines()
        del id_note[id_del - 1]
        with open("data.txt", "w") as f:
            for item in id_note:
                f.write(item)
        file.close()
def delete_in_id():
    print("Заметку можно удалить по ID")
    with open("data.txt") as file:
        id_del = input()
        id_note = file.readlines()

    with open("data.txt", "w") as f:
        for item in id_note:
            if ("id: " + id_del + "; ") not in item:
                f.write(item)
        file.close()
def delete_in():
    print("Удалить заметку можно по ID или номеру строки: \n 1 - ID \n 2 - номер строки \n 0 - выход \n")
    com = int(input())
    if com == 1:
        delete_in_id()
    elif com == 2:
        deleteData()
    elif com == 0:
        return