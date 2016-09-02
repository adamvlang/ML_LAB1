import monkdata as m
import math
import dtree

monk1_entropy = dtree.entropy(m.monk1)
monk2_entropy = dtree.entropy(m.monk2)
monk3_entropy = dtree.entropy(m.monk3)

print(monk1_entropy)
print(monk2_entropy)
print(monk3_entropy)

