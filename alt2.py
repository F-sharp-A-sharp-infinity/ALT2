import csv  # csv library makes going through data a lot easier
import matplotlib.pyplot as plt  # plotting library
import statistics
start_of_week = 1595795742  # sets initial unix time for the start of the first week (hardcoded)
week_list = [start_of_week]  # makes a week list that never gets used
art_dict = dict()  # makes the empty master dictionary

with open('lastfmalt.csv', newline='', encoding="utf-8") as f:  # opening the csv file
    reader = csv.reader(f)  # using the csv library to set up a reader option which...
    for row in reader:  # we can go through row by row with this for statement. each row is a list
        if row[-2] == "":  # checking this item isn't null avoids errors, if it is we just skip the row
            pass  # does nothing, which is what we want
        else:  # the actual main body of the code occurs within this else statement
            if int(row[-2]) - 604800 >= start_of_week:  # if its been more than a week since start_of_week's value
                for artist, art_values in art_dict.items():  # goes through every artist in our list
                    if not art_values.keys().__contains__(start_of_week):  # if the artist doesn't have a key for this week
                        art_dict[artist][start_of_week] = 0  # make a key for the week with zero plays
                start_of_week += 604800  # update the start of the week
                week_list.append(start_of_week)  # add it to the week list
            if row[0] in art_dict.keys():  # if the artist is already in our dictionary of artists
                if list(art_dict[row[0]].keys())[-1] == start_of_week:  # if the last key added to the artist is the same as the current start of week
                    art_dict[row[0]][start_of_week] += 1  # increase that key/week's plays by one
                else:  # if the artist doesn't have the current week
                    art_dict[row[0]][start_of_week] = 1  # add it and set the value to one
            else:  # if the artist isn't in our dictionary
                art_dict[row[0]] = {start_of_week: 1}  # make a dictionary called the artist's name and give it the current week and set it's value to one

top_artist = ["placeholder", 0]
bottom_artist = ["placeholder", 10000]
artist_mean_total = 0
artist_median_dict = dict()
top_artist_dict = dict()

for artist, weeks in art_dict.items():
    art_total = 0
    for i in weeks.values():
        art_total += i
    artist_mean_total += art_total
    artist_median_dict[artist] = art_total
    if art_total >= 179:  # play around with this value to display a good amount of artists
        plt.plot(weeks.keys(), weeks.values(), label=artist)
        top_artist_dict[artist] = art_total
    elif art_total >= 50:
        plt.plot(weeks.keys(), weeks.values())
    if art_total > top_artist[1]:
        top_artist = [artist, art_total]
    if art_total < bottom_artist[1]:
        bottom_artist = [artist, art_total]

artist_mean_total = artist_mean_total / len(art_dict.keys())
print("the median number of plays is", statistics.median(artist_median_dict.values()))
print("the modal number of plays is", statistics.mode(artist_median_dict.values()))
print("artist with maximum plays is", top_artist[0], "with", top_artist[1], "plays")
print("artist with minimum plays is", bottom_artist[0], "with", bottom_artist[1], "plays")
print("the (mean) average number of plays is", artist_mean_total)
for artist, plays in top_artist_dict.items():
    print(artist, "appears", plays, "times in this data set")

plt.title("Plays by week")
plt.ylabel("Plays")
plt.xlabel("week")
plt.legend(loc='upper left')
plt.show()


