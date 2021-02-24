
import csv
import matplotlib.pyplot as plt
ng = 0
gybe = 0
ng_months = {
    "Jul": 0,  # these should match how the date was outputted by: https://mainstream.ghan.nl/export.html
    "Aug": 0,
    "Sep": 0,
    "Oct": 0,
    "Nov": 0,
    "Dec": 0,
    "Jan": 0,
}
g_list = []
n_list = []
# csv should have artist in column 1 and date format w/3 letter month in column 5
with open('test8.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row.__contains__("Godspeed You! Black Emperor"):
            print(row)
            for i in ng_months:
                if row[4].__contains__(i):
                    ng_months[i] += 1
for key, value in ng_months.items():
    temp = [key, value]
    g_list.append(temp[1])


with open('test8.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row.__contains__("Nana Grizol"):
            for i in ng_months:
                if row[4].__contains__(i):
                    ng_months[i] += 1
for key, value in ng_months.items():
    temp = [key, value]
    n_list.append(temp[1])

print(g_list)
plt.plot(g_list)
plt.plot(n_list)
plt.legend(["gybe plays", "nana grizol plays"])
plt.title("plays by month")
plt.ylabel("plays")
plt.xlabel("months since start of account")
plt.show()

import csv
import matplotlib.pyplot as plt
months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
ng_months = dict()
gybe_months = dict()
for month in months:
    ng_months[month] = 0
    gybe_months[month] = 0
# csv should have artist in some columng and date format w/3 letter month in column 2
with open('test8.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row.__contains__("Godspeed You! Black Emperor"):
            print(row)
            for i in gybe_months:
                if row[-1].__contains__(i):
                    gybe_months[i] += 1
        if row.__contains__("Nana Grizol"):
            for i in ng_months:
                if row[-1].__contains__(i):
                    ng_months[i] += 1

plt.title("Plays by month")
plt.ylabel("Plays")
plt.xlabel("Month")
plt.plot(ng_months.keys(), ng_months.values(), label='Nana Grizol')
plt.plot(gybe_months.keys(), gybe_months.values(), label="Godspeed You! Black Emperor")
plt.legend()
plt.show()
