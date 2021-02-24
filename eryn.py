import csv


def readbook(filename):
    with open(filename, newline='') as openbook:
        big = []
        reader = csv.reader(openbook)
        for row in reader:
            string = ""
            for i in row:
                string += i
                big.append(string.split(" "))

            return big


aList = readbook("AliceInWonderland.csv")
dList = readbook("Dracula.csv")
pList = readbook("PeterPan.csv")
jbList = readbook("TheJungleBook.csv")
sgList = readbook("TheSecretGarden.csv")

wordList = []
wordCount = 0
print(type(aList[1]))
#print(totalWords)

for item in aList:
    if not item.isalpha():
        break
    else:
        if item in wordList:
            pass
        else:
            wordList.append(item)
            wordCount = wordCount + 1
print(wordCount)