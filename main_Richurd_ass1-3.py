import monkdata as m
import math
import dtree
import random 

# Assignment 1 #
################

monk_entropy = []
data_sets = [m.monk1, m.monk2, m.monk3]
for set in data_sets:
    monk_entropy.append(dtree.entropy(set))
print('\nentropy: ')
for i in range(3):
    print(monk_entropy[i])
print('\n')


# Assignment 2 #
################

monk_gain = []
attributes = m.attributes
for set in data_sets:
	for i in range(6):
		monk_gain.append(dtree.averageGain(set, attributes[i]))
	i=0
print("Gain table: \n", monk_gain[0:5],  "\n",  monk_gain[6:11],  "\n",  monk_gain[12:17], "\n")


# Assignment 3 #
################

t=dtree.buildTree(m.monk1, m.attributes)
print(dtree.check(t, m.monk1test))
t=dtree.buildTree(m.monk2, m.attributes)
print(dtree.check(t, m.monk2test))
t=dtree.buildTree(m.monk3, m.attributes)
print(dtree.check(t, m.monk3test))


# Assignment 4 #
################

def partition(data, fraction):
	ldata = list(data)
	random.shuffle(ldata)
	breakPoint = int(len(ldata) * fraction)
	return ldata[:breakPoint], ldata[breakPoint:]
monk1train, monk1val = partition(m.monk1, 0.8)

print("Pruning: ")
t=dtree.buildTree(monk1train, m.attributes)
print(dtree.check(t, monk1val))
"""
t=dtree.buildTree(m.monk2, m.attributes)
print(dtree.check(t, monk2val))
t=dtree.buildTree(m.monk3, m.attributes)
print(dtree.check(t, monk3val))
"""

################

print("\n\n\n\n\n\n\n\n")