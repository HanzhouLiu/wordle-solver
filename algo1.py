"""
A wordle solver written in python from scratch.
Information theory method.
Date: Apr 24, 2022
"""

"""
Parameters:
wordlist:   the wordlist, long or short.
"""
import enum
from tasks import tasks
from tasks import entropy
import numpy as np
import math

class algo:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.size = len(wordlist)
        
        #self.width = np.base_repr(3**5, base=3)
    
    def colorInfo(self):
        colors = ["green", "yellow", "gray"]
        #length = np.base_repr(3**5, base=3)
        #i = int()
        colorsComb = []
        for i in range(3**5):
            colorinfo = []
            vector = np.base_repr(i, base=3, padding=5)
            for j in range(5):
                bit = vector[-j-1]
                colorinfo.append(colors[int(bit)])
            colorsComb.append(colorinfo)
            # print(colorinfo, '\n')    # no gray in the color infor list

        return colorsComb
        print("the first row in colorsComb", colorsComb)
        print("length of colorsComb: ", len(colorsComb))


    def rest(self):
        e_arr = np.zeros((self.size, 3**5))
        row = 0
        restDict = {}
        for word in self.wordlist:
            mylist = []
            for comb in self.colorInfo():
                combStr = "{} {} {} {} {}".format(comb[0], comb[1], comb[2], comb[3], comb[4])
                rest = tasks(self.wordlist, word, colors=combStr).word_filter(False)
                restNum = len(rest)
                mylist.append(restNum)
            dict = {word: mylist}
            restDict.update(dict)     
        # print(restDict)
        return(restDict)
        #for key, val in enumerate(restDict.items()):
        #    val.remove(0)
        #    e = val[n] for n in val
    
    """
    wordsEntropy is used to get a dictionary
    key: word in the wordlist
    guess: the word with the largest entropy
    """
    def maxEntropy(self):
        restDict = self.rest()
        mydict = {}
        for key in restDict:
            mydict[key] = entropy(restDict[key])
            
        # print(mydict)
        # print(type(mydict))

        guess = max(mydict, key=mydict.get)
        print("Our guess is: ", guess)
        return mydict, guess

# alphaFile = open("wordle-list/short-list", "r")
# alpha = []

# for line in alphaFile:
#     # print("word", word)
#     word = line.split("\n") # exclude the "\n" in .txt
#     alpha.append(word[0]) 

# algo(wordlist=alpha).colorInfo() 
# algo(wordlist=alpha).maxEntropy()