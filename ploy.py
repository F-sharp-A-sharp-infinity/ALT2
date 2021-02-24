import matplotlib.pyplot as plt
"""""
names = ["Alex", "James", "Aidan", "Ciara", "Jeff", "Ellen"]
times = [7, 12, 37, 30, 14, 26]

plt.bar(names, times)
plt.title("walks to school")
plt.ylabel("time in minutes")
plt.xlabel("student")
plt.show()
"""""
d = {"Alex": 7,
         "james": 12,
         "aidan": 37
         }
plt.bar(range(len(d)), d.values(), align="center")
plt.xticks(range(len(d)), list(d.keys()))
plt.title("walks to school")
plt.ylabel("time in minutes")
plt.xlabel("student")
plt.show()