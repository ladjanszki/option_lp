''' 
This file has all the test code to demonstrate the input generation functionality works

The first example is a CRR tree. The European vanilla calls value have to be 33.33333
Second the normalized example from the lecture. Have to evaluate to 0.09
Third  

'''
from treelib import Node, Tree
import util

# CRR tree
crrTree = Tree()
crrTree.create_node("0", "0", data=util.StateData([1, 100], 0))  # root node
crrTree.create_node("1", "1", parent="0", data=util.StateData([1, 200], 100))
crrTree.create_node("2", "2", parent="0", data=util.StateData([1, 50], 0))
#crrTree.show(data_property="secPrice")
#crrTree.show(data_property="payOff")

util.treeToLp(crrTree, 'inputs/crr.lp')

# Lecture example (normalised)
nTree = Tree()
nTree.create_node("0", "0", data=util.StateData([1, 1, 1], 0))  # root node
nTree.create_node("1", "1", parent="0", data=util.StateData([1, 0.713178294573643, 0.821705426356589], 0))
nTree.create_node("2", "2", parent="0", data=util.StateData([1, 9.53846153846154, 6.30769230769231], 0))
nTree.create_node("3", "3", parent="1", data=util.StateData([1, 0.652892561983471, 1.00826446280992], 0))
nTree.create_node("4", "4", parent="1", data=util.StateData([1, 0.634328358208955, 0.850746268656716], 0))
nTree.create_node("5", "5", parent="1", data=util.StateData([1, 0.848484848484848, 0.621212121212121], 0.090909090909091))
nTree.create_node("6", "6", parent="2", data=util.StateData([1, 9.53846153846154, 6.30769230769231], 1.84615384615385))
#nTree.show(data_property="secPrice")
#nTree.show(data_property="payOff")

# Lecture example (unnormalized)
unTree = Tree()
unTree.create_node("0", "0", data=util.StateData([100, 100, 100], 0))  # root node
unTree.create_node("1", "1", parent="0", data=util.StateData([129, 92, 106], 0))
unTree.create_node("2", "2", parent="0", data=util.StateData([6.5, 62, 41], 0))
unTree.create_node("3", "3", parent="1", data=util.StateData([121, 79, 122], 0))
unTree.create_node("4", "4", parent="1", data=util.StateData([134, 85, 114], 0))
unTree.create_node("5", "5", parent="1", data=util.StateData([132, 112, 82], 12))
unTree.create_node("6", "6", parent="2", data=util.StateData([13, 124, 82], 24))

#unTree.show(data_property="secPrice")
#unTree.show(data_property="payOff")

outTree = util.normalizeTree(unTree)

#outTree.show(data_property="secPrice")
#outTree.show(data_property="payOff")


util.treeToLp(outTree, 'inputs/tmp.lp')




