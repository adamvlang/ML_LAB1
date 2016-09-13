import monkdata as m
import math
import dtree
import random 

# Assignment 1 #
################
print("-----------------------------------------------------------------------------------------------------")
monk_entropy = []
data_sets = [m.monk1, m.monk2, m.monk3]
for set in data_sets:
    monk_entropy.append(dtree.entropy(set))
print('\nEntropy: ')
for i in range(3):
    print(monk_entropy[i])
print('\n')


# Assignment 2 #
################
i = 0
monk_gain = []
attributes = m.attributes
for set in data_sets:
	for i in range(6):
		monk_gain.append(dtree.averageGain(set, attributes[i]))
	i=0

print("Gain table assignment 2: \n", monk_gain[0:6],  "\n",  monk_gain[6:12],  "\n",  monk_gain[12:18], "\n")

# Assignment 3 #
################

data_set_Monk1att5EqualTo1 = dtree.select(data_sets[0], attributes[4], 1) #Create dataset with attributes A2=1

entropy_Monk1att2 = dtree.entropy(data_set_Monk1att5EqualTo1)
print("Entropy Monk1 Attribute A5=1: ", entropy_Monk1att2)

data_set_Monk1att5EqualTo2 = tuple(dtree.select(data_sets[0], attributes[4], 2))
data_set_Monk1att5EqualTo3 = tuple(dtree.select(data_sets[0], attributes[4], 3))
data_set_Monk1att5EqualTo4 = tuple(dtree.select(data_sets[0], attributes[4], 4))

entropy_Monk1att5EqualTo2 = dtree.entropy(data_set_Monk1att5EqualTo2)
entropy_Monk1att5EqualTo3 = dtree.entropy(data_set_Monk1att5EqualTo3)
entropy_Monk1att5EqualTo4 = dtree.entropy(data_set_Monk1att5EqualTo4)
print("Entropy Monk1 Attribute A5=2: ", entropy_Monk1att5EqualTo2)
print("Entropy Monk1 Attribute A5=3: ", entropy_Monk1att5EqualTo3)
print("Entropy Monk1 Attribute A5=4: ", entropy_Monk1att5EqualTo4)


data_set_Level_2 = [data_set_Monk1att5EqualTo2, data_set_Monk1att5EqualTo3, data_set_Monk1att5EqualTo4]
i = 0
monk_gain = []
attributes = m.attributes
for set in data_set_Level_2:
	for i in range(6):
		monk_gain.append(dtree.averageGain(set, attributes[i]))
	i=0
print("\nGain table for second nodes: \n", monk_gain[0:6],  "\n",  monk_gain[6:12],  "\n",  monk_gain[12:18], "\n")




t=dtree.buildTree(m.monk1, m.attributes)
print("% of correctly classified samples in monk1test: ", dtree.check(t, m.monk1test))
monkTEST1 = dtree.check(t, m.monk1test)
print(t)
t=dtree.buildTree(m.monk2, m.attributes)
print("% of correctly classified samples in monk2test: ", dtree.check(t, m.monk2test))
#print(t)
t=dtree.buildTree(m.monk3, m.attributes)
print("% of correctly classified samples in monk3test: ", dtree.check(t, m.monk3test))
#print(t)
print("\n")


# Assignment 4 #
################

def partition(data, fraction):
	ldata = list(data)
	random.shuffle(ldata)
	breakPoint = int(len(ldata) * fraction)
	return ldata[:breakPoint], ldata[breakPoint:]
monk1train, monk1val = partition(m.monk1, 0.8) #monk1train is the trainingset, monk1val is the validationset

print("length of training: ", len(monk1train))
print("length of validation: ", len(monk1val))

print("Pruning Monk1: ")
t=dtree.buildTree(monk1train, m.attributes)
#print(dtree.check(t, monk1val))
#while :

listOfTrees = ()

print("ListOfTrees type: ", type(listOfTrees))
bestTreeOld = 11234
listOfBetterTrees = 0
while listOfBetterTrees != 15:
	try:
		listOfTrees = dtree.allPruned(t)
	except:
		print("No more possibilitys!")
		break
	print("number of available tree alternatives: ", len(listOfTrees))
	#bestTree = ()
	for tree in range(len(listOfTrees)):
		print("tree: ", tree)

		print(dtree.check(listOfTrees[tree], monk1val))
		if dtree.check(listOfTrees[tree], monk1val) > monkTEST1:
			monkTEST1 = dtree.check(listOfTrees[tree], monk1val)
			bestTree = listOfTrees[tree]
			print("Number on best tree", tree)
	t=bestTree
	if bestTree == bestTreeOld:
		break
	bestTreeOld = bestTree
	listOfBetterTrees = listOfBetterTrees + 1
	print("BEST POSSIBLE: ", bestTree)
	print(dtree.check(listOfTrees[tree], monk1val))
print("Best Tree EVER: ", bestTree)
#print("BEST POSSIBLE: ", dtree.check(bestPossibleTree, m.monk1test))
################

print(dtree.check(bestTree, m.monk1test))

print("Pruning Monk3: ")

print("\n\n\n\n\n\n\n\n")