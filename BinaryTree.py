from Node import Node

class BinaryTree:
    root = None

    def __init__(self):
        print("Tree created")

    def Add(self, value):
        if self.root == None:
            self.root = Node(value)