from Node import Node

class BinaryTree:
    root = None

    def __init__(self):
        print("Tree created")

    def __str__(self):
        print(self.root.value)
        self.root.Print("")

    def Add(self, value):
        if self.root == None:
            self.root = Node(value)
            #print("Root was zero, new Node created")
        else: 
            self.root.AddValue(value)
            #print("Root wasn't zero, other Node created")

    def Print(self):
        if self.root != None:
            self.root.PrintValues()
        else:
            print("Tree is empty, nothing here to print")
