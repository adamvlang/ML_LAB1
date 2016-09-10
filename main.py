import monkdata as m
import math
import dtree


# Assignment 1 #
################

#Setting up lists
monk_entropy = []
data_sets = [m.monk1, m.monk2, m.monk3]

#calculating entropy of the monk sets
for set in data_sets:
    monk_entropy.append(dtree.entropy(set))

#print(monk_entropy)

# Assignment 2 #
################

#Setting up lists
info_gain_m1 = []
info_gain_m2 = []
info_gain_m3 = []
attribute = []

#starting counter
i = 0;
#iterating over all the test sets
for sets in [info_gain_m1, info_gain_m2, info_gain_m3]:

    #for all attributes in the sets, the average information gain is added to the list
    for k in range(6):
        attribute.append(dtree.averageGain(data_sets[i], m.attributes[k]));
    sets.append(attribute)

    attribute = []
    i += 1;
    
#print(info_gain_m1)
#print(info_gain_m2)
#print(info_gain_m3)

# Assignment 3 #
################

selected = dtree.select(m.monk1, m.attributes[4], 1)

t=dtree.buildTree(m.monk1, m.attributes);
print(dtree.check(t, m.monk1test))

print(t)
