"""
A wordle solver written in python from scratch.
Information theory method.
Date: Apr 24, 2022
"""
from algo1 import algo
from wordle import wordle
from tasks import tasks

SEED = 0

Count = 0

alphaFile = open("wordle-list/short-list", "r")
alpha = []

for line in alphaFile:
    # print("word", word)
    word = line.split("\n") # exclude the "\n" in .txt
    alpha.append(word[0]) 

print("How many words do we have in the wordlist: ", len(alpha))
Start = wordle(alpha, SEED).answer()
print("The correct answer is: {} \n".format(Start))
Rest = list(alpha)

while len(Rest) != 0:
    Count += 1
    #print("length of Rest list: ", len(Rest))
    myDict, Guess = algo(wordlist=Rest).maxEntropy()
    Colors = wordle(alpha, SEED).feedback(Guess)
    Rest = list(tasks(Rest, word=Guess, colors=Colors).word_filter(reorder=False))
    print("length of Rest list: ", len(Rest))
    print("What are the remaining words in the list: \n {}\n".format(Rest))
    if Colors == "green green green green green":
        break
    # alpha = list(Rest)

Colors = wordle(alpha, SEED).feedback(Guess)
print("How many guesses did we try: ", Count)
print("Our guess is: ", Guess)
#print("The number of total words in alphabet: ", len(alpha))
#print("The first word in the list: ", alpha[0])
#print("test ends")

