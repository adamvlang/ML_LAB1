import monkdata as m
import math
import dtree


# Assignment 1 #
################

monk_entropy = []
data_sets = [m.monk1, m.monk2, m.monk3]

i = 0
for set in data_sets:
    monk_entropy.append(dtree.entropy(set))
    i += 1

for i in range(3):
    print(monk_entropy[i])

# Assignment 2 #
################
