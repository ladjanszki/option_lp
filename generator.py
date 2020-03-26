import numpy as np

class Node:
    def __init__(self):
        self.number = -1
        self.securities = []
        self.child = []
       
    def __str__(self):
        return "World state number: " + str(self.number) + " Num sec: " + str(len(self.securities)) + " Num chil: " + str(len(self.child))

    def addChild(self):
        self.child.append(Node())

class Tree:
    def __init__(self, numLevel, numBranch):
        self.root = Node()
        self.maxWSN = -1
        self.numSecurities = 0



root = Node()
root.number = 0
root.securities = [1, 100]

print(root)

root.addChild()

print(root)


        




