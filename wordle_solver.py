"""
A wordle solver written in python from scratch.
Information theory method.
Date: Apr 24, 2022
"""
from cupshelpers import Printer
from algo1 import algo
from wordle import wordle
from tasks import tasks

SEED = 1

Count = 1

alphaFile = open("wordle-list/short-list", "r")
alpha = []

for line in alphaFile:
    # print("word", word)
    word = line.split("\n") # exclude the "\n" in .txt
    alpha.append(word[0]) 

print("How many words do we have in the wordlist: ", len(alpha))
Start = wordle(alpha, SEED).answer()
print("The correct answer is: ", Start)
Rest = list(alpha)

while len(Rest) != 1:
    #print("length of Rest list: ", len(Rest))
    myDict, Guess = algo(wordlist=Rest).maxEntropy()
    Colors = wordle(alpha, SEED).feedback(Guess)
    Rest = list(tasks(Rest, word=Guess, colors=Colors).word_filter(reorder=False))
    print("length of Rest list: ", len(Rest))
    print(Rest)
    # alpha = list(Rest)

    Count += 1

print("How many guesses did we try: ", Count)
print("Our guess is: ", Guess)

#print("The number of total words in alphabet: ", len(alpha))
#print("The first word in the list: ", alpha[0])
#print("test ends")

