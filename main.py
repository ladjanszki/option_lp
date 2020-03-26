from treelib import Node, Tree

class StateData:
    def __init__(self, secPrice, payOff):
        self.secPrice = secPrice
        self.payOff = payOff

    def __str__(self):
        return str(self.secPrice)

# Generating a tree of prices
tree = Tree()

tree.create_node("0", "0", data=StateData([1, 100], 0))  # root node
tree.create_node("1", "1", parent="0", data=StateData([1, 200], 100))
tree.create_node("2", "2", parent="0", data=StateData([1, 50], 0))

# Draw tree
#tree.show(data_property="secPrice")

# Store all variable names in this list during traversing
allVarNames = []

# Generating the objective function from the root element
rootNode = tree[tree.root] 
objFunc= []

# Adding name
objFunc.append("OBJ: ")


# Adding root node variables
for idx, sec in enumerate(rootNode.data.secPrice):
    objFunc.append("{0:+16.4f} th{1:08d}_{2:08d} ".format(float(sec), int(rootNode.tag), int(idx)))
    #Saving variable names for bounds section
    allVarNames.append("th{0:08d}_{1:08d} free".format(int(rootNode.tag), int(idx)))


#print('allVarNames')
#print(allVarNames)

    
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
                actLine.append("{0:+16.4f} th{1:08d}_{2:08d} ".format(-float(sec), int(actNode.tag), int(idx)))

            #Adding child variables
            for idx, sec in enumerate(actCh.data.secPrice):
                actLine.append("{0:+16.4f} th{1:08d}_{2:08d} ".format(float(sec), int(actCh.tag), int(idx)))
                #Saving variable names for bounds section
                allVarNames.append("th{0:08d}_{1:08d} free".format(int(actCh.tag), int(idx)))

            #Adding the right hand side
            #TODO: Shouldnt write -0
            actLine.append("= {0:+16.4f}".format(-float(actCh.data.payOff)))

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
            actLine.append("{0:+16.4f} th{1:08d}_{2:08d} ".format(float(sec), int(actNode.tag), int(idx)))


        #Adding the right hand side
        actLine.append(">= 0")

        # Adding line to list for later file assembly
        nnConst.append(''.join(actLine))
        #print(''.join(actLine))

        nnNum = nnNum + 1

# Assembling the input file
with open('generated.lp', mode='wt', encoding='utf-8') as myfile:

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


