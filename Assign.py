from typing import List, Any

lineList = list()
f = open('Sonnet.txt', 'r')
with open('Sonnet.txt') as f:
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
def ladderLength(beginWord, endWord, wordList):
    """

    :type beginWord: object
    """
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    # BFS visit
    curr_level = {beginWord}
    dist = 1
    while curr_level:
        wordList -= curr_level
        next_level = set()
        for word in curr_level:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word == endWord:
                        return 1 + dist
                    if new_word in wordList:
                        next_level.add(new_word)
        curr_level = next_level
        dist += 1
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


print(ladderLength(start1, target1, Lists))
print(ladderLength(start2, target2, Lists))
print(ladderLength(start3, target3, Lists))
print(ladderLength(start4, target4, Lists))
print(ladderLength(start5, target5, Lists))
print(ladderLength(start6, target6, Lists))
print(ladderLength(start7, target7, Lists))
print(ladderLength(start8, target8, Lists))
print(ladderLength(start9, target9, Lists))
print(ladderLength(start10, target10, Lists))
