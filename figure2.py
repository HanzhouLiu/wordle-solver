"""
Draw the figure for Experiment 2.0.
Our guess is RAISE: Entropy = 5.87830295649317.
mamma has the Minimum Entropy 2.2687228440411724.
average entropy: 4.505974168031054.
"""
# importing the module
import ast
import matplotlib.pyplot as plt


def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key

# reading the data from the file
with open('expers/exper2.txt') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
myDict = ast.literal_eval(data)

print("Data type after reconstruction : ", type(myDict))

exper2ListWord = myDict.keys()
exper2ListEntropy = myDict.values()
print("RAISE's entropy: ", myDict['raise'])
min_entropy = min(exper2ListEntropy)
print("{} has the Minimum Entropy {}".format(get_key(myDict, min_entropy), min_entropy))

plt.figure(figsize=(6, 6))

#plt.subplot(111)
fig2 = plt.scatter(exper2ListWord, exper2ListEntropy)
plt.ylabel('Entropy')
plt.xlabel('Five-letter Words')
fig2.axes.xaxis.set_visible(False)
plt.show()