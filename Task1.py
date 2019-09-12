from collections import Counter
f = open('Sonnet3.txt', 'r')
lineList = f.readlines()
inputText = int(input("Enter number between 1 and 11: "))
isCorrect = False
if inputText >= 1 and inputText <= 11:
    teststr = lineList[inputText - 1]
    data = lineList[inputText - 1].split(" ")
    isCorrect = True
else:
    print("Enter valid number 1 to 11")

if isCorrect:
    count = 0
    fre = 'abcdefghijklmnopqrstuvwxyz'

    # A

    for j in fre:
        j = j.lower()
        k = j.upper()
        print(j + " " + str(teststr.count(j)) +"     "+ k + " " + str(teststr.count(k)))







    print(data)
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    for j in data:
        if len(j) == 1:
            count1 = count1 + 1
        elif len(j) == 2:
            count2 = count2 + 1
        elif len(j) == 3:
            count3 = count3 + 1
        elif len(j) == 4:
            count4 = count4 + 1
        elif len(j) == 5:
            count5 = count5 + 1
        elif len(j) == 6:
            count6 = count6 + 1
        elif len(j) == 7:
            count7 = count7 + 1
        elif len(j) == 8:
            count8 = count8 + 1
        elif len(j) == 9:
            count9 = count9 + 1
        elif len(j) == 10:
            count10 = count10 + 1

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


    counts = dict()
    for word in data:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print(counts)