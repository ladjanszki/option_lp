from treelib import Node, Tree
import numpy as np

import util


# We always have the same random numbers
np.random.seed(0)


#### HF1
# arg: filename
# arg: startPrices (list)
# arg: branches on levels (tuple)
# arg: mean, sigma (random generator parameters)
lpFileName = 'inputs/hf1.lp'
#lpFileName = 'debug.lp'

#tree = Tree()
#tree.create_node("0", "0", data=util.StateData([1, 100, 100, 100], 0))  # root node
#
#for idx in range(1,101):
#    tree.create_node('0/' + str(idx), '0/' + str(idx), parent="0", data=util.stateDataIterator(tree['0'], 2, 1))

# New tree builder
tree = util.treeGenerator((100, ), [1, 100, 100, 100], 2, 1)
#tree = util.treeGenerator((100, 100), [1, 100, 100, 100], 2, 1)


#tree.show(data_property='representation')
#tree.show(data_property="secPrice")
#tree.show(data_property="payOff")

# Postprocessing a tree for payoffs
util.calculatePayoffs(tree)

#tree.show(data_property='representation')
#tree.show(data_property="secPrice")
#tree.show(data_property="payOff")
tree.show()

# Generating the GLPK input
util.treeToLp(tree, lpFileName)





 




##### HF2
#tree = Tree()
#tree.create_node("0", "0", data=util.StateData([1, 100, 100, 100], 0))  # root node
#
#for idx in range(1,1001):
#    tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0']))
#
## Postprocessing a tree for payoffs
#util.calculatePayoffs(tree)
#
## Generating the GLPK input
#util.treeToLp(tree, 'inputs/hf2.lp')
#
##### HF3
#tree = Tree()
#tree.create_node("0", "0", data=util.StateData([1, 100, 100, 100], 0))  # root node
#
#for idx in range(1,10001):
#    tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0']))
#
## Postprocessing a tree for payoffs
#util.calculatePayoffs(tree)
#
## Generating the GLPK input
#util.treeToLp(tree, 'inputs/hf2.lp')
#
##### HF4
#tree = Tree()
#tree.create_node("0", "0", data=util.StateData([1, 100, 100, 100], 0))  # root node
#
#for idx in range(1,100001):
#    tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0']))
#
## Postprocessing a tree for payoffs
#util.calculatePayoffs(tree)
#
## Generating the GLPK input
#util.treeToLp(tree, 'inputs/hf2.lp')
 
 
 
 
