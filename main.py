from treelib import Node, Tree
import util

class StateData:
    def __init__(self, secPrice, payOff):
        self.secPrice = secPrice
        self.payOff = payOff

    def __str__(self):
        return str(self.secPrice)


# Generating a tree of prices
tree = Tree()

# CRR tree
#tree.create_node("0", "0", data=StateData([1, 100], 0))  # root node
#tree.create_node("1", "1", parent="0", data=StateData([1, 200], 100))
#tree.create_node("2", "2", parent="0", data=StateData([1, 50], 0))

# Lecture example
tree.create_node("0", "0", data=StateData([1, 1, 1], 0))  # root node
tree.create_node("1", "1", parent="0", data=StateData([1, 0.713178294573643, 0.821705426356589], 0))
tree.create_node("2", "2", parent="0", data=StateData([1, 9.53846153846154, 6.30769230769231], 0))
tree.create_node("3", "3", parent="1", data=StateData([1, 0.652892561983471, 1.00826446280992], 0))
tree.create_node("4", "4", parent="1", data=StateData([1, 0.634328358208955, 0.850746268656716], 0))
tree.create_node("5", "5", parent="1", data=StateData([1, 0.848484848484848, 0.621212121212121], 0.090909090909091))
tree.create_node("6", "6", parent="2", data=StateData([1, 9.53846153846154, 6.30769230769231], 1.84615384615385))

# Draw tree
#tree.show(data_property="secPrice")
#tree.show(data_property="payOff")


util.treeToLp(tree)
 


