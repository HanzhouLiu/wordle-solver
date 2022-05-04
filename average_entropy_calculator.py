import ast

with open('expers/exper2.txt') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
myDict = ast.literal_eval(data)

exper2ListEntropy = myDict.values()
print(exper2ListEntropy)

Sum = 0
for e in exper2ListEntropy:
    Sum += e
averageEntropy = Sum / len(exper2ListEntropy)
print(averageEntropy)