import enum
from tasks import tasks
from tasks import entropy
from wordle import wordle
from algo1 import algo
import numpy as np
import math
import timeit

"""
Experiment 1: Check how many guesses it takes to get a correct answer.

Experiment 2: Check the entropy distribution of the whole word list. 
"""


class experimets:
    def __init__(self, wordlist):
        self.wordlist = wordlist
    
    def exper1(self, times):
        print("Start\n")
        with open("expers/exper1.txt", "w") as f1:
            for i in range(times):
                print("Play {}th game".format(i))
                Count = 0
                print("How many words do we have in the wordlist: ", len(alpha))
                Start = wordle(self.wordlist, i).answer()
                print("The correct answer is: ", Start)
                Rest = list(self.wordlist)
                timerStart = timeit.default_timer()
                while len(Rest) != 0:
                    Count += 1
                    #print("length of Rest list: ", len(Rest))
                    myDict, Guess = algo(wordlist=Rest).maxEntropy()
                    Colors = wordle(self.wordlist, i).feedback(Guess)
                    
                    Rest = list(tasks(Rest, word=Guess, colors=Colors).word_filter(reorder=False))
                    #print("length of Rest list: ", len(Rest))
                    #print("What are the remaining words in the list: \n", Rest)
                    # alpha = list(Rest)
                    
                    if Colors == "green green green green green":
                        break
                timerStop = timeit.default_timer()
                f1.write('{} rounds to guess {} within {} seconds\n'.format(Count, Start, timerStop - timerStart))

                print("How many guesses did we try: ", Count)
                print("Our guess is: ", Rest[0])
    
    def exper2(self):
        print("Start Experiment 2\n")
        with open("expers/exper2.txt", "w") as f2:
            f2.write('{}'.format(algo(self.wordlist).maxEntropy()[0]))
    
    # Colors: a string
    def exper3(self, Word, Colors):
        rest = tasks(alpha, word=Word, colors=Colors).word_filter(False)
        print(rest)
        return rest
    
    def exper4(self):
        # print(algo(wordlist=alpha).maxEntropy()[0])
        with open("expers/exper4.txt", "w") as f2:
            f2.write('{}'.format(algo(self.wordlist).maxEntropy()[0]))
    
alphaFile = open("wordle-list/short-list", "r")
alpha = []

for line in alphaFile:
    # print("word", word)
    word = line.split("\n") # exclude the "\n" in .txt
    alpha.append(word[0]) 


# Do Experiment 1
# experimets(wordlist=alpha).exper1(times=50)

# Do Experiment 2
# experimets(wordlist=alpha).exper2()

# Do Experiment 3
# print("The word-list's size is: {}".format(len(alpha)))
# Rest = experimets(wordlist=alpha).exper3("raise", "gray gray gray gray gray")
# print("Given the word and color information, the word-list's size is: {}".format(len(Rest)))

# Do Experiment 4
# None