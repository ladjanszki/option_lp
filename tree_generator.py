from treelib import Node, Tree
import numpy as np

import util


tree = util.treeGenerator((10, 10), [1, 100, 100, 100], 2, 1)

util.calculatePayoffs(tree)

#tree.show()
tree.show(data_property="secPrice")
tree.show(data_property="payOff")

