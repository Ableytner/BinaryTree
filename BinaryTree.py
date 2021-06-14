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
            self.root.Print("")
        else:
            print("Tree is empty, nothing here to print")

    def Print2(self):
        if self.root != None:
            data = ["└──── " + str(self.root.value)]
            self.root.Print2(data, 0, 0)
            for x in data:
                print(x)
        else:
            print("Tree is empty, nothing here to print")

    def display(self):
        lines, *_ = self.root._display_aux()
        for line in lines:
            print(line)


