"""
The experiment is based on the short-word list, which has 2309 words.
The average is AVERAGE(2*2+3*16+4*26+5*4+6*2) = 3.76.
"""

import matplotlib.pyplot as plt


exper1File = open("expers/exper1.txt", "r")
exper1List = []

for line in exper1File:
    # print("word", word)
    round = line.split(" ")[0] # exclude the "\n" in .txt
    exper1List.append(int(round)) 
print(exper1List)

def get_number_of_elements(list, target):
    count = 0
    for item in list:
        if target == item:
            count += 1
    return count

myDict = {}
for num in [2, 3, 4, 5, 6]:
    myDict[num] = get_number_of_elements(exper1List, num)
print(myDict)

rounds = list(myDict.keys())
rounds_pie = ['2 guesses', '3 guesses', '4 guesses', '5 guesses', '6 guesses']
wordsNum = list(myDict.values())
print(rounds, wordsNum)

plt.figure(figsize=(6, 6))

#plt.subplot(111)
plt.bar(rounds, wordsNum)
plt.ylabel('Number of Games')
plt.xlabel('Number of Guesses in a Single Game')

#plt.subplot(122)
explode = (0, 0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(wordsNum, explode=explode, labels=rounds_pie, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.figure(figsize=(6, 6))
plt.suptitle('the Number of Guesses to Get the Answer')
plt.show()

# 
