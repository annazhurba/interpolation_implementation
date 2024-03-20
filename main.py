import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


def interpolacja_lagrange(x, dystans_do_interpolacji, wysokosc_do_interpolacji):
    n = len(dystans_do_interpolacji)
    result = 0

    for i in range(n):
        y = wysokosc_do_interpolacji[i]
        for j in range(n):
            if i != j:
                y *= (x - dystans_do_interpolacji[j])/(dystans_do_interpolacji[i] - dystans_do_interpolacji[j])
        result += y

    return result


#żeby zmienić liczbę węzłów interpolacji, należy zmienić liczbę przepisaną do zmiennej krok
k = 5
file = 'GlebiaChallengera.csv'

f = open(file, 'r')
data = list(csv.reader(f))
data.pop(0)

data = data[1:50]
dystans = []
wysokosc = []

for i in range(len(data)):
    dystans.append(float(data[i][0]))
    wysokosc.append(float(data[i][len(data[0]) - 1]))

plt.plot(dystans, wysokosc, label="pelne dane")
plt.xlabel("Dystans (m)")
plt.ylabel("Wysokosc (m)")
plt.title(file)
plt.show()

wysokosc_do_interpolacji = wysokosc[1::k]
dystans_do_interpolacji = dystans[1::k]

# interpolacja Lagrange'a
wysokosc_po_interpolacji = [interpolacja_lagrange(x, dystans_do_interpolacji, wysokosc_do_interpolacji) for x in dystans]


plt.plot(dystans, wysokosc, 'r.', label="pelne dane")
plt.plot(dystans, wysokosc_po_interpolacji, label="interpolowane")
#plt.ylim(0, 3000)
plt.xlabel("Dystans (m)")
plt.ylabel("Wysokosc (m)")
plt.title(file + ", k = " + str(k) + ", " + str(len(wysokosc_po_interpolacji)) + " punktow")

plt.show()





