from treelib import Node, Tree
import numpy as np

import util

#subtreeTuple = (2, 3, 5)
#print(subtreeTuple[1:])


def levelBuilder(tree, parentId, subtreeTuple):
    for nChild in range(subtreeTuple[0]):

        actId = str(parentId) + '_' + str(nChild)
        tree.create_node(str(actId), str(actId), parent=str(parentId))

        # If note the leaf level, call level builder recursively
        if len(subtreeTuple) > 1:
            levelBuilder(tree, actId, subtreeTuple[1:])



# Creating a tree
tree = Tree()

# Adding root node
tree.create_node('0', '0')  


levelBuilder(tree, '0', (2, 3, 5))

tree.show()
#crrTree.show(data_property="payOff")




#for idx in range(1,101):
#    # Adding first level nodes
#    tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0'], 2, 1))
#
#    for idx in range(1,101):
#        # Adding second level node
#        tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0'], 2, 1))
#
## Postprocessing a tree for payoffs
#util.calculatePayoffs(tree)
#
## Generating the GLPK input
#util.treeToLp(tree, lpFileName)
# 
#
#
#
##### HF1
## arg: filename
## arg: startPrices (list)
## arg: branches on levels (tuple)
## arg: mean, sigma (random generator parameters)
#lpFileName = 'inputs/hf1.lp'
#
#tree = Tree()
#tree.create_node("0", "0", data=util.StateData([1, 100, 100, 100], 0))  # root node
#
#for idx in range(1,101):
#    tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0'], 2, 1))
#
## Postprocessing a tree for payoffs
#util.calculatePayoffs(tree)
#
## Generating the GLPK input
#util.treeToLp(tree, lpFileName)

 
