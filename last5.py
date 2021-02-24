import csv
import matplotlib.pyplot as plt
gybe = 0
g_list = [0]
k_list = [0]
n_list = [0]
m_list = [0]
time_temp = 26
with open('test9.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row.__contains__("Godspeed You! Black Emperor"):
            tee = row[4]
            tee = tee[0:2]
            temp = int(tee)
            print(temp)
            if temp == time_temp:
                g_list[-1] += 1
            else:
                g_list.append(1)
                time_temp = temp


print(g_list)
print(k_list)
print(len(g_list))
plt.plot(g_list)
plt.title("gybe plays daily")
plt.ylabel("plays")
plt.xlabel("days since start of account")
plt.show()

