file = open("Random100.csv", "r")
dataIn = file.read()
file.close()
myList = []
dataIn = dataIn.split(",")
for item in dataIn:
    if item != "":
        myList.append(int(item))
for value in myList:
    if value > 30:
        myList[value-1] = 30
print(myList)
myList.sort()
print(myList)
