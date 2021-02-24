import csv
import matplotlib.pyplot as plt
temp = 0
counter = 0
g_list = [0]
k_list = []
c_list =[]
time_temp = 1595795742
with open('test9.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        if row.__contains__("Godspeed You! Black Emperor"):
            row[3] = int(row[3])
            if row[3] - 604800 > time_temp:
                g_list.append(1)
                time_temp = row[3]
            else:
                g_list[-1] += 1
with open('hse.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        k_list.append(row[1])
    for i in k_list:
        temp += int(i)
        counter += 1
        if counter == 7:
            c_list.append(temp)
            counter = 0

val = max(c_list) // max(g_list)
for i in range(len(g_list)):
    g_list[i] = g_list[i]*val

print(c_list)
print(g_list)
print(len(g_list), len(c_list))
plt.plot(c_list)
plt.plot(g_list)
plt.title("gybe vs covid")
plt.ylabel("% of max plays/cases")
plt.xlabel("week since start of account")
plt.show()

