import csv
import matplotlib.pyplot as plt
gybe = 0
g_list = [0]
k_list = [0]
n_list = [0]
m_list = [0]
time_temp = 1595795742
time_temp1 = 1595795742
with open('test9.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row.__contains__("Godspeed You! Black Emperor"):
            row[3] = int(row[3])
            if row[3] - 604800 > time_temp:
                g_list.append(1)
                time_temp = row[3]
            else:
                g_list[-1] += 1
        elif row.__contains__("Nana Grizol"):
            row[3] = int(row[3])
            if row[3] - 604800 > time_temp1:
                k_list.append(1)
                time_temp1 = row[3]
            else:
                k_list[-1] += 1

print(g_list)
print(k_list)
print(len(g_list))
plt.plot(g_list)
plt.plot(k_list)
plt.title("plays by month")
plt.ylabel("plays")
plt.xlabel("months since start of account")
plt.show()

