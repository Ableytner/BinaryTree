

class Node:
    left = None
    right = None
    value = 0

    def __init__(self, data):
        self.value = data

    def Print(self, before):
        if self.left != None and self.right != None:
            print(before + "├── " + str(self.left.value))
            self.left.Print()
            print(before + "└── " + str(self.right.value))
            self.left.Print()
            return ""
        if self.left != None and self.right == None:
            print(before + "└── " + str(self.left.value))
            self.left.Print()
            return ""
        if self.right != None and self.left == None:
            print(before + "└── " + str(self.right.value))
            self.right.Print()
            return ""


    def PrintValues(self):
        if self.left != None:
            self.left.PrintValues()

        if self.right != None:
            self.right.PrintValues()

        print(self.value, end = " ")

    def AddValue(self, value):
        if(self.value > value):
            if(self.left != None):
                print("Going left")
                self.left.AddValue(value)
            else:
                self.left = Node(value)
                print("Left Node created")
        else:
            if(self.right != None):
                print("Going right")
                self.right.AddValue(value)
            else:
                self.right = Node(value)
                print("Right Node created")
           