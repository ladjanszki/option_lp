from treelib import Node, Tree
import numpy as np

class StateData:
    '''
    Class containing the finance specific data in a tree node
    '''
    def __init__(self, secPrice, payOff):
        self.secPrice = secPrice
        self.payOff = payOff

    def __str__(self):
        return "Prices: " + str(self.secPrice) + " PayOff: " + str(self.payOff)

    def normalize(self):
        ''' Returning a normalized copy of itself '''
        return StateData([x / self.secPrice[0] for x in self.secPrice], self.payOff / self.secPrice[0])


def stateDataIterator(sd):
    ''' 
    The function returns a valid child world state of the one in the argument
    '''

    # Change of the price of stocks
    newSecPrice = [0.5 * 100 + 0.5 * x + np.random.lognormal(2, 1) - np.exp(2.5)  for x in sd.data.secPrice]
 
    # Cash always 1
    newSecPrice[0] = 1

    return StateData(newSecPrice, sd.data.payOff)

def calculatePayoffs(tree):
    '''
    Traversing a tree and calculating the payoffs for all leaf nodes

    The contingent claim is an exchange option
    The function works in place overwriting any preexisting values
    '''

    for nodeId in tree.expand_tree(mode=Tree.DEPTH):
        actNode = tree[nodeId]
    
        # Calculate payoff for leaf nodes
        if actNode.is_leaf():  
            actNode.data.payOff = np.maximum(0, actNode.data.secPrice[2] - actNode.data.secPrice[1])
 

def normalizeTree(tree):
    '''
    Normalizing a tree (undestructive method, copy to another tree)

    '''

    outTree = Tree()
    for nodeId in tree.expand_tree(mode=Tree.DEPTH):
        actNode = tree[nodeId]
    
        # Copy node by node and normalize
        if actNode.is_root():  # The root node has no parent
            outTree.create_node(actNode.tag, actNode.identifier, data=actNode.data.normalize())
        else: # A non root node has parent
            outTree.create_node(actNode.tag, actNode.identifier, parent=actNode.bpointer, data=actNode.data.normalize())

    return outTree

def treeToLp(tree, outFileName):
    '''
    Function to transform a price tree into a linear programming input

    The output is in the LP format for GLPK solver

    '''

    # Store all variable names in this list during traversing
    allVarNames = []
    
    # Generating the objective function from the root element
    rootNode = tree[tree.root] 
    objFunc= []
    
    # Adding name
    objFunc.append("OBJ: ")
    
    
    # Adding root node variables
    for idx, sec in enumerate(rootNode.data.secPrice):
        #objFunc.append("{0:+20.16f} th{1:08d}_{2:08d} ".format(float(sec), int(rootNode.tag), int(idx)))
        objFunc.append("{0:+20.16f} th{1:d}_{2:d} ".format(float(sec), int(rootNode.tag), int(idx)))
        #Saving variable names for bounds section
        #allVarNames.append("th{0:08d}_{1:08d} free".format(int(rootNode.tag), int(idx)))
        allVarNames.append("th{0:d}_{1:d} free".format(int(rootNode.tag), int(idx)))
        
    # Traversing the tree for constrints
    sfNum = 1 # Index for the self financing constraint
    nnNum = 1 # Index for the non negativity constraint
    sfConst = [] #List for self financing constraints
    nnConst = [] #List for non negativity constraints
    for nodeId in tree.expand_tree(mode=Tree.DEPTH):
    
        actNode = tree[nodeId]
    
        # If node has child then adding a self financing constraint
        if not actNode.is_leaf(): # Non leaf node
            
            # Loop on children
            for chId in actNode.fpointer:
    
                # Print a line for every children
                actLine = []
    
                actCh = tree[chId]
       
                #Adding the constrint name
                actLine.append("SF{0:08d}: ".format(sfNum))
    
                #Adding Parent variables
                for idx, sec in enumerate(actCh.data.secPrice):
                    #actLine.append("{0:+20.16f} th{1:08d}_{2:08d} ".format(-float(sec), int(actNode.tag), int(idx)))
                    actLine.append("{0:+20.16f} th{1:d}_{2:d} ".format(-float(sec), int(actNode.tag), int(idx)))
    
                #Adding child variables
                for idx, sec in enumerate(actCh.data.secPrice):
                    #actLine.append("{0:+20.16f} th{1:08d}_{2:08d} ".format(float(sec), int(actCh.tag), int(idx)))
                    actLine.append("{0:+20.16f} th{1:d}_{2:d} ".format(float(sec), int(actCh.tag), int(idx)))
                    #Saving variable names for bounds section
                    #allVarNames.append("th{0:08d}_{1:08d} free".format(int(actCh.tag), int(idx)))
                    allVarNames.append("th{0:d}_{1:d} free".format(int(actCh.tag), int(idx)))
    
                #Adding the right hand side
                #TODO: Shouldnt write -0
                actLine.append("= {0:+20.16f}".format(-float(actCh.data.payOff)))
    
                # Adding line to list for later file assembly
                sfConst.append(''.join(actLine))
                #print(''.join(actLine))
    
                sfNum = sfNum + 1
    
        # If node is leaf adding a Non negativity constraint
        else: # Leaf node
    
    
            # Print a line for every children
            actLine = []
            
            #Adding constraint name
            actLine.append('NN{0:08d}: '.format(nnNum))
    
    
            #Adding Parent variables
            for idx, sec in enumerate(actNode.data.secPrice):
                #actLine.append("{0:+20.16f} th{1:08d}_{2:08d} ".format(float(sec), int(actNode.tag), int(idx)))
                actLine.append("{0:+20.16f} th{1:d}_{2:d} ".format(float(sec), int(actNode.tag), int(idx)))
    
    
            #Adding the right hand side
            actLine.append(">= 0")
    
            # Adding line to list for later file assembly
            nnConst.append(''.join(actLine))
            #print(''.join(actLine))
    
            nnNum = nnNum + 1
    
    # Assembling the input file
    with open(outFileName, mode='wt', encoding='utf-8') as myfile:
    
        myfile.write('MIN\n')
        myfile.write(''.join(objFunc))
        myfile.write('\n')
        myfile.write('\n')
        myfile.write('SUBJECT TO\n')
        myfile.write('\n'.join(sfConst))
        myfile.write('\n')
        myfile.write('\n')
        myfile.write('\n'.join(nnConst))
        myfile.write('\n')
        myfile.write('\n')
        myfile.write('BOUNDS\n')
        myfile.write('\n'.join(allVarNames))
        myfile.write('\n')
        myfile.write('\n')
        myfile.write('END\n')
 
