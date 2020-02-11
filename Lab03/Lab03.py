import matplotlib.pyplot as plt
import numpy as np

#test = "((((((((((((.......)))))))))...))).."
#test2 = "GGCCGCGGCAGGUUCGAGUCCUGCCGCGAUCGCCAC"

s1 = []
AUUA = 0
CGGC = 0
GUUG = 0
total = 0
parenList = []
RNA = []

with open("trna_seq_out.txt") as l:
    nuc = {'A', 'G', 'U', 'C'}
    test = []
    test2 = []
    for line in l:
        if line[0] in nuc:
            RNA = line
        if line[0] == '(' or line[0] == '.':
            parenList = line.split()
            index = 0
            for f in parenList[0]:
                if f == '(':
                    s1.append(index)
                if f == ')':
                    j = s1.pop()
                    total += 1

                    if RNA[index] == 'A':
                        AUUA += 1
                    elif RNA[index] == 'C':
                        CGGC += 1
                    elif RNA[index] == 'G':
                        if RNA[j] == 'C':
                            CGGC += 1
                        else:
                            GUUG += 1
                    elif RNA[index] == 'U':
                        if RNA[j] == 'A':
                            AUUA += 1
                        else:
                            GUUG += 1
                index += 1

print(AUUA/total * 100, CGGC/total * 100, GUUG/total * 100)
print(total)

#graph for Ecoli
objects1 = ('AU-UA', 'CG-GC', 'GU-UG')
y_pos = np.arange(len(objects1))
performance = [AUUA/total * 100, CGGC/total * 100, GUUG/total * 100]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects1)
plt.ylabel('Percentages')
plt.xlabel('Pairs')

plt.show()
