file = open("test8.csv", "r", encoding="utf-8")
dataIn = file.read()
file.close()
myList = dataIn.split("")
print(myList[0:100])
print(len(myList))
"""""
junk = 0
for i in myList:
    if i.__contains__("Yes"):
        junk += 1


print(junk)

"""""
