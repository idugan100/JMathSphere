import matplotlib.pyplot as plt
import numpy as np
import csv
file = open("Price.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

data = np.array(data, dtype=float).flatten()

fig, ax = plt.subplots()

ax.hist(data, bins=50, linewidth=0.5, edgecolor="white"), plt.xticks([2.5+i*.1 for i in range(25)])

plt.show()

fig, ax2 = plt.subplots()

ax2.boxplot(data)
plt.show()
