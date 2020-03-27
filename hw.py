from treelib import Node, Tree
import numpy as np

import util


# We always have the same random numbers
np.random.seed(0)


# HF1
tree = Tree()
tree.create_node("0", "0", data=util.StateData([1, 100, 100, 100], 0))  # root node

for idx in range(1,101):
    tree.create_node(str(idx), str(idx), parent="0", data=util.stateDataIterator(tree['0']))


#tree.show(data_property="secPrice")

# Postprocessing a tree for payoffs
util.calculatePayoffs(tree)
#tree.show(data_property="payOff")


util.treeToLp(tree, 'inputs/hf1.lp')
 
