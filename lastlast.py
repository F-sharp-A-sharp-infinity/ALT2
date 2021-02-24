"""""
to use this code unchanged you'll need to get your data using this exporter: https://mainstream.ghan.nl/export.html
in your data editor of choice set column 1 to the artist, the second from last to the unix time, and the rest 
don't matter. remove the headers and sort from lowest unix time to highest. set the filename in line 12 to whatever your
file is called. change start_of_week and week_list to the first unix time value in your data.
"""""
import csv
import matplotlib.pyplot as plt
start_of_week = 1595795742
week_list = [start_of_week]
art_list = dict()
with open('lastfmalt.csv', newline='', encoding="utf-8") as f:  # read in my last.fm data
    reader = csv.reader(f)
    # count number of plays per week for each artist
    for row in reader:
        if row[1] == "":
            pass
        else:
            if int(row[1]) - 604800 >= start_of_week:  # just don't worry about anything from here to line 31
                for artist, art_values in art_list.items():
                    if not art_values.keys().__contains__(start_of_week):
                        art_list[artist][start_of_week] = 0
                start_of_week += 604800
                week_list.append(start_of_week)
            if row[0] in art_list.keys():
                if list(art_list[row[0]].keys())[-1] == start_of_week:
                    art_list[row[0]][start_of_week] += 1
                else:
                    art_list[row[0]][start_of_week] = 1
            else:
                art_list[row[0]] = {
                    start_of_week: 1
                }

                date = int(row[-1][0:2])

print(art_list)

for artist, weeks in art_list.items():
    art_total = 0
    for i in weeks.values():
        art_total += i
    if art_total >= 179:  # play around with this value to display a good amount of artists
        plt.plot(weeks.keys(), weeks.values(), label=artist)
    else:
        plt.plot(weeks.keys(), weeks.values())  # comment this out to remove all the unlabeled lines
        pass

plt.title("Plays by week")
plt.ylabel("Plays")
plt.xlabel("week")
plt.legend(loc='upper left')
plt.show()
