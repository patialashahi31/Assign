from typing import List, Any

lineList = list()
f = open('Sonnet1.txt', 'r')
with open("Sonnet1.txt") as f:
    for line in f:
        for s in line:
            lineList.append(line)

teststr = lineList[0]
count = 0
freq = {}
# A
for i in teststr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Count of all characters:\n " + str(freq))

# B
data = lineList[0].split(" ")
print(data)
count1 = 0;
count2 = 0;
count3 = 0;
count4 = 0;
count5 = 0;
count6 = 0;
count7 = 0;
count8 = 0;
count9 = 0;
count10 = 0;
for j in data:
    if len(j) == 1:
        count1 = count1 + 1;
    elif len(j) == 2:
        count2 = count2 + 1;
    elif len(j) == 3:
        count3 = count3 + 1;
    elif len(j) == 4:
        count4 = count4 + 1;
    elif len(j) == 5:
        count5 = count5 + 1;
    elif len(j) == 6:
        count6 = count6 + 1;
    elif len(j) == 7:
        count7 = count7 + 1;
    elif len(j) == 8:
        count8 = count8 + 1;
    elif len(j) == 9:
        count9 = count9 + 1;
    elif len(j) == 10:
        count10 = count10 + 1;

print("One letter word " + str(count1))
print("Two letter word " + str(count2))
print("Three letter word " + str(count3))
print("Four letter word " + str(count4))
print("Five letter word " + str(count5))
print("Six letter word " + str(count6))
print("Seven letter word " + str(count7))
print("Eight letter word " + str(count8))
print("Nine letter word " + str(count9))
print("Ten letter word " + str(count10))

# C
counts = dict()
for word in data:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)



# 2)
def minladder(beg, end, list):
    """

    :type beginWord: object
    """
    list = set(list)
    if end not in list:
        return 0

    curr = {beg}
    res = 1
    while curr:
        list -= curr
        next = set()
        for word in curr:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new = word[:i] + c + word[i + 1:]
                    if new == end:
                        return 1 + res
                    if new in list:
                        next.add(new)
        curr = next
        res += 1
    return 0


Lists = open('Words.txt').read().splitlines()

start1 = "flour"
target1 = "bread"
start2 = "chaos"
target2 = "peace"
start3 = "river"
target3 = "shore"
start4 = "sleep"
target4 = "dream"
start5 = "black"
target5 = "white"
start6 = "witch"
target6 = "fairy"
start7 = "tears"
target7 = "smile"
start8 = "which"
target8 = "think"
start9 = "paper"
target9= "story"
start10 = "early"
target10 = "trees"


print(minladder(start1, target1, Lists))
print(minladder(start2, target2, Lists))
print(minladder(start3, target3, Lists))
print(minladder(start4, target4, Lists))
print(minladder(start5, target5, Lists))
print(minladder(start6, target6, Lists))
print(minladder(start7, target7, Lists))
print(minladder(start8, target8, Lists))
print(minladder(start9, target9, Lists))
print(minladder(start10, target10, Lists))
