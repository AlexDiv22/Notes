from Input import inputData

def writeData():
    file = open('data.txt', 'a')
    data = inputData()
    file.write("Id: " + data[0] + "; ")
    file.write("Дата: " + data[1] + "; ")
    file.write("Заголовок: " + data[2] + "; ")
    file.write("Содержание: " + data[3] + "; \n")
    file.close()
    print("Заметка создана" + "\n")