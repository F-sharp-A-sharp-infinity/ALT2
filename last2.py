import matplotlib.pyplot as plt
import csv
ng_months = {  # dictionary so we can store values for each month
    "Jul": 0,
    "Aug": 0,
    "Sep": 0,
    "Oct": 0,
    "Nov": 0,
    "Dec": 0,
    "Jan": 0,
}  # this csv has rows where each row is a play of a song and the first row is the artist and 5th row is the date
with open('test8.csv', newline='', encoding="utf-8") as f:  # opens the csv
    reader = csv.reader(f)  # sets up the reader object
    for row in reader:  # for each row in the reader object ie the csv
        if row.__contains__("Godspeed You! Black Emperor"):  # if the row contains this artist name
            for i in ng_months:  # for each key in the dictionary
                if row[4].__contains__(i):  # if the row with the date contains i
                    ng_months[i] += 1  # increase the value of i by one
# just plotting stuff frome here
plt.bar(range(len(ng_months)), ng_months.values(), align="center")
plt.xticks(range(len(ng_months)), list(ng_months.keys()))
plt.title("Godspeed You! Black Emperor plays by month")
plt.ylabel("plays")
plt.xlabel("month")
plt.show()
