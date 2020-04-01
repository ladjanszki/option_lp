from treelib import Node, Tree
from subprocess import PIPE, run
import numpy as np

import util


# Reproducible random numbers
np.random.seed(0)

# HW1
task_id = 'hw1'
inputFileName = 'inputs/' + task_id + '.lp'
outFileName = 'outs/' + task_id + '.out'
tree = util.treeGenerator(childrenPerLevel = (100, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
util.calculatePayoffs(tree) 
util.treeToLp(tree, inputFileName) # Generating the GLPK input


command = ['glpsol', '--lp', inputFileName, '-o',  outputFileName]
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
#print(result.returncode, result.stdout, result.stderr)

exit(0)


# HW2
lpFileName = 'inputs/hw2.lp'
tree = util.treeGenerator(childrenPerLevel = (1000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
util.calculatePayoffs(tree) 
util.treeToLp(tree, lpFileName) # Generating the GLPK input

# HW3
lpFileName = 'inputs/hw3.lp'
tree = util.treeGenerator(childrenPerLevel = (10000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
util.calculatePayoffs(tree) 
util.treeToLp(tree, lpFileName) # Generating the GLPK input
 
# HW4
lpFileName = 'inputs/hw4.lp'
tree = util.treeGenerator(childrenPerLevel = (100000, ), initSecPrice = [1, 100, 100, 100], logNormalMean = 2, logNormalSigma = 1) 
util.calculatePayoffs(tree) 
util.treeToLp(tree, lpFileName) # Generating the GLPK input
 


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
 
 
 
 
