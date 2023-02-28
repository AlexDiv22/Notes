import csv

def readData():
    file = open('data.csv', 'r')
    reader = csv.reader(file)
    for line in reader:
        print(line)
    file.close()
    print()