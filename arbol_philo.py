from treelib import Node, Tree
tree = Tree()
tree.create_node("", "ABCD")
tree.create_node("D", "D", parent="ABCD")
tree.create_node("0.4", "ABC", parent="ABCD")
tree.create_node("C", "C", parent="ABC")
tree.create_node("0.05", "AB", parent="ABC")
tree.create_node("B", "B", parent="AB")
tree.create_node("A", "A", parent="AB")
 
tree.show()
