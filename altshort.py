import csv  # csv library makes going through data a lot easier
import matplotlib.pyplot as plt  # plotting library for chart
import statistics  # statistics library for median and mode
start_of_week = 1595795742  # sets initial unix time for the start of the first week (hardcoded)
art_dict = dict()  # makes the empty master dictionary

with open('lastfmalt.csv', newline='', encoding="utf-8") as file:  # opening the csv file
    reader = csv.reader(file)  # using the csv library to set up a reader option which...
    for row in reader:  # we can go through row by row with this for statement. each row is a list
        if row[1] == "":  # checking this item isn't null avoids errors, if it is we just skip the row
            pass  # does nothing, which is what we want
        else:  # the actual main body of the code occurs within this else statement
            if int(row[1]) - 604800 >= start_of_week:  # if its been more than a week since start_of_week's value
                for artist, art_values in art_dict.items():  # goes through every artist in our list
                    if not art_values.keys().__contains__(start_of_week):  # if the artist doesn't have a key for this week
                        art_dict[artist][start_of_week] = 0  # make a key for the week with zero plays
                start_of_week += 604800  # update the start of the week
            if row[0] in art_dict.keys():  # if the artist is already in our dictionary of artists
                if list(art_dict[row[0]].keys())[-1] == start_of_week:  # if the last key added to the artist is the same as the current start of week
                    art_dict[row[0]][start_of_week] += 1  # increase that key/week's plays by one
                else:  # if the artist doesn't have the current week
                    art_dict[row[0]][start_of_week] = 1  # add it and set the value to one
            else:  # if the artist isn't in our dictionary
                art_dict[row[0]] = {start_of_week: 1}  # make a dictionary called the artist's name and give it the current week and set it's value to one

top_artist = ["placeholder", 0]  # list to store top artist name and number of plays
bottom_artist = ["placeholder", 10000]  # list to store top artist name and number of plays
artist_mean_total = 0  # value to add to to calculate mean
artist_median_dict = dict()  # dictionary to store artists an their total plays for median
top_artist_dict = dict()  # dictionary to store most played artists an their total plays

for artist, weeks in art_dict.items():  # go through every artist and their associated dictionary
    art_total = 0  # sets the total plays for the current artist to zero at the start
    for i in weeks.values():  # goes through the total weekly plays for the current artist
        art_total += i  # adds them to the artist total
    artist_mean_total += art_total  # adds the current artist's total to the total for the mean plays
    artist_median_dict[artist] = art_total  # adds the current artist and their total to the dictionary for median plays
    if art_total >= 100:  # play around with this value to display a good amount of artists
        plt.plot(weeks.keys(), weeks.values(), label=artist)  # plots current artist on the line chart and adds their name to the legend
        top_artist_dict[artist] = art_total  # adds the artist to the top artist dictionary
    elif art_total >= 50:  # comment this and the next line out to just see top artists
        plt.plot(weeks.keys(), weeks.values())  # plots current artist on the line chart
    if art_total > top_artist[1]:  # if the artist's total plays is greater than the value currently stored
        top_artist = [artist, art_total]  # set the list to now contain the new artist name and total
    if art_total < bottom_artist[1]:  # if the artist's total plays is less than the value currently stored
        bottom_artist = [artist, art_total]  # set the list to now contain the new artist name and total

artist_mean_total = artist_mean_total / len(art_dict.keys())  # divide the total plays overall by the number of artists
print("the median number of plays is", statistics.median(artist_median_dict.values()))  # prints median
print("the modal number of plays is", statistics.mode(artist_median_dict.values()))  # prints mode
print("artist with maximum plays is", top_artist[0], "with", top_artist[1], "plays")  # prints maximum
print("artist with minimum plays is", bottom_artist[0], "with", bottom_artist[1], "plays")  # prints minimum
print("the (mean) average number of plays is", artist_mean_total)  # prints mean
for artist, plays in top_artist_dict.items():  # goes through top artists
    print(artist, "appears", plays, "times in this data set")  # prints their frequency

plt.title("Plays by week")  # sets title of chart
plt.ylabel("Plays")  # sets y axis label to plays
plt.xlabel("week")  # sets x axis label to week (unix time value that isn't human friendly unfortunately)
plt.legend(loc='upper left')  # adds the legend and places it in the upper left corner
plt.show()  # displays the chart


