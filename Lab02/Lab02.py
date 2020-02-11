import sys

#redone with alg from class notes

"""
for i in range(0, 9):
    for j in range (0, 9):
        for k in range (0, 9):
            print(i, j, k)
"""

def permm(n, coins):
    i = []
    for c in coins:
        i.append(int(n/c))
    return i

def arrayStuff(list):
    highNum = ''
    for i in range(0, len(list)):
        highNum += str(list[i])

    highNum = int(highNum)
    print(highNum)

    permList = [str(i).zfill(len(list)) for i in range(0, highNum)]
    return permList

def bruteForceChange(n, coins, d):
    bestArr = []
    smallestNumCoins = float("inf")

    p = permm(n, coins)
    p2 = arrayStuff(p)

    for a in p2:
        value = 0
        for i in range(0, d):
            value += int(a[i]) * c[i]
        if value == n:
            numCoins = 0
            #gives num coins that makes solution
            for j in range(0,d):
                numCoins += int(a[j])
            if numCoins < smallestNumCoins:
                smallestNumCoins = numCoins
                bestArr = a
    return[bestArr, smallestNumCoins]

n = 6
c = (25, 20, 10, 5, 1)
d = 5
print(bruteForceChange(n,c,d))

