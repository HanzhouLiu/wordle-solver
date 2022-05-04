"""
A wordle generator
wordlist:   the input word list
seedNum:    the random seed used to generate the correct word
guess:      the input guess word
"""
import random

#alphaFile = open("wordle-list/short-list", "r")
#alpha = []

#for line in alphaFile:
#    # print("word", word)
#    word = line.split("\n") # exclude the "\n" in .txt
#    alpha.append(word[0]) 

class wordle:
    def __init__(self, wordlist, seedNum):
        self.size = len(wordlist)
        self.alpha = wordlist
        random.seed(seedNum)
        self.start = wordlist[random.randint(0, self.size-1)]

    def answer(self):
        return self.start

    def feedback(self, guess):
        print("correct answer is: ", self.start)
        colorInfo = []
        for idx, letter in enumerate(guess):
            if letter == self.start[idx]:
                colorInfo.append('green')
            if letter not in self.start:
                colorInfo.append('gray')
            if letter in self.start and letter != self.start[idx]:
                colorInfo.append('yellow')
        colorsStr = "{} {} {} {} {}".format(colorInfo[0], colorInfo[1], colorInfo[2], colorInfo[3], colorInfo[4])
        print("color information string is: ", colorsStr)
        return(colorsStr)

# wordle(alpha, 1).feedback("taste")