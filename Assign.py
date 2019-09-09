import collections
from typing import List, Any


f = open('Sonnet3.txt', 'r')
lineList = f.readlines()
aaa = int(input("Enter number between 1 and 11:  11"))
if(aaa==1):
    teststr = lineList[0]
    data = lineList[0].split(" ")
if(aaa==2):
    teststr = lineList[1]
    data = lineList[1].split(" ")
if(aaa==3):
    teststr = lineList[2]
    data = lineList[2].split(" ")
if(aaa==4):
    teststr = lineList[3]
    data = lineList[3].split(" ")
if(aaa==5):
    teststr = lineList[4]
    data = lineList[4].split(" ")
if(aaa==6):
    teststr = lineList[5]
    data = lineList[5].split(" ")
if(aaa==7):
    teststr = lineList[6]
    data = lineList[6].split(" ")
if(aaa==8):
    teststr = lineList[7]
    data = lineList[7].split(" ")
if(aaa==9):
    teststr = lineList[8]
    data = lineList[8].split(" ")
if(aaa==10):
    teststr = lineList[9]
    data = lineList[9].split(" ")
if(aaa==11):
    teststr = lineList[10]
    data = lineList[10].split(" ")
else:
    print("Enter valid number 1 to 11")



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



#2)
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
target9 = "story"
start10 = "early"
target10 = "trees"





def minladder( beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    combine = collections.defaultdict(list)
    x = len(beginWord)
    for word in wordList:
        for i in range(x):
            combine[word[0:i] + "*" + word[i + 1:]].append(word)


    queue, paths, dis = collections.deque([(beginWord, [beginWord])]), [], {}
    while queue:
        word, path = queue.popleft()
        for i in range(x):
            key = word[0:i] + "*" + word[i + 1:]
            for w in combine[key]:
                # avoid loop visit
                if w in dis and dis[w] <= len(path):
                    continue
                dis[w] = len(path) + 1

                if w == endWord and (not paths or len(path) + 1 <= len(paths[-1])):
                    paths.append(path + [w])
                    break
                queue.append((w, path + [w]))

    if not paths:
        return []
    return [paths[0]]


print("Flour and bread: " + str(minladder(start1, target1, Lists)))
print("Chaos and peace: " + str(minladder(start2, target2, Lists)))
print("River and shore: " + str(minladder(start3, target3, Lists)))
print("Sleep and dream: " + str(minladder(start4, target4, Lists)))
print("Black and white: "  + str(minladder(start5, target5, Lists)))
print("Witch and fairy: "  + str(minladder(start6, target6, Lists)))
print("tears and smile: "  + str(minladder(start7, target7, Lists)))
print("which and think: "  + str(minladder(start8, target8, Lists)))
print("paper and story: "  + str(minladder(start9, target9, Lists)))
print("early and trees: "  + str(minladder(start10, target10, Lists)))