"""
Parameters:
wordlist: the wordlist, long or short;
word: the nst guess, a 5-letter string to be converted to a list;
colors: the color info in each spot, a list 
        of "yellow" "green" or "gray".
"""
import math


class tasks:
    def __init__(self, wordlist, word, colors):
        self.wordlist = wordlist
        self.word = list(word)
        self.colors = colors.split()

    def dict(self, reorder=False):
        if reorder:
            pass
        else:
            dict = {idx: [letter, self.colors[idx]] for idx, letter in enumerate(self.word)}

        return dict

    def letter_filter(self, idx, letter, color, inlist):
        # remove words from the input list based on the letter's color info
        outlist = []
        if color == 'green':
            for item in inlist:
                if item[idx] == letter:
                    outlist.append(item)
        if color == 'gray':
            for item in inlist:
                if letter not in item:
                    outlist.append(item)
        if color == 'yellow':   # not gray or green
            for item in inlist:
                if (item[idx] != letter) and (letter in item):
                    outlist.append(item) 
        
        return outlist
                
    def word_filter(self, reorder=False):
        # remove words from the word list based on the word's color info
        if reorder:
            pass
        else:
            my_list = list(self.wordlist)
            for key, val in self.dict(reorder).items():
                # print(key, val)
                val_letter = val[0]
                val_color = val[1]
                # print(key, val_letter, val_color)
                my_list = list(
                    self.letter_filter(idx=key, letter=val_letter, color=val_color, inlist=my_list))
        
        return my_list
    
def entropy(list):
    # list.remove(0)
    Sum = sum(list)
    # print("Sum = ", Sum)
    result = 0
    for num in list:
        if num == 0:
            e = 0
        else:
            p = num/Sum
            e = p*math.log(1/p, 2)
        result += e
    return result


# alphaFile = open("wordle-list/short-list", "r")
# alpha = []

# for line in alphaFile:
#     # print("word", word)
#     word = line.split("\n") # exclude the "\n" in .txt
#     alpha.append(word[0]) 
        

# info = tasks(alpha, word="songs", colors="yellow green gray gray gray").dict(False)
# print(info)

# rest = tasks(alpha, word="songs", colors="gray green gray yellow gray").word_filter(False)
# print(rest)
# print(len(rest))