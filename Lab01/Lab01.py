import matplotlib.pyplot as plt
import numpy as np
import string

#thermo counts
letterCounter = dict(zip(string.ascii_lowercase,[0]*26))
total = 0
with open("Thermo.txt") as f:
    for line in f:
        for word in line.split():
            for letter in list(word.lower()):
                letterCounter[letter]+=1
                total+=1

for i in letterCounter:
    if letterCounter.values() == 0:
        pass
    else:
        letterCounter[i] = letterCounter[i] / total

print("thermo")
print(letterCounter)
print(total)

f.close()

#ecoli counts
letterCounter2 = dict(zip(string.ascii_lowercase,[0]*26))
total2 = 0

with open("Ecoli.txt") as f2:
    for line in f2:
        for word in line.split():
            for letter in list(word.lower()):
                letterCounter2[letter]+=1
                total2+=1

for i in letterCounter2:
    if letterCounter2.values() == 0:
        pass
    else:
        letterCounter2[i] = letterCounter2[i] / total2

print("ecoli")
print(letterCounter2)
print(total2)

f2.close()


#graph for Thermophile
objects = ('G', 'C', 'T', 'A')
y_pos = np.arange(len(objects))
performance = [31.89546112193373,31.751577379199064,18.207584001246127,18.145]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Percentages')
plt.title('Thermophile Genome Makeup')

plt.show()

"""
#graph for Ecoli
objects1 = ('C', 'G', 'T', 'A')
y_pos = np.arange(len(objects1))
performance = [25.441712775434777,25.188812774889185,24.661890684223203,24.707583765452834]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects1)
plt.ylabel('Percentages')
plt.xlabel('Ecoli Genome Makeup')

plt.show()
"""

