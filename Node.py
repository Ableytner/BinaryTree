

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
                #print("Going left")
                self.left.AddValue(value)
            else:
                self.left = Node(value)
                #print("Left Node created")
        else:
            if(self.right != None):
                #print("Going right")
                self.right.AddValue(value)
            else:
                self.right = Node(value)
                #print("Right Node created")

    def Print2(self, data, before, index):
        if self.left != None and self.right != None:
            data.insert(index, "|" + self.GetSpaces(5) + self.GetSpaces(before) + "┌──── " + str(self.left.value))
            data.insert(index + 1, "|" + self.GetSpaces(5) + self.GetSpaces(before) + "└──── " + str(self.right.value))
            self.left.Print2(data, before + 6, index)
            self.right.Print2(data, before + 6, index + 1)
            return
        if self.left != None:
            data.insert(index, "|" + self.GetSpaces(5) + self.GetSpaces(before) + "┌──── " + str(self.left.value))
            self.left.Print2(data, before + 6, index)
            return
        if self.right != None:
            data.insert(index + 1, "|" + self.GetSpaces(5) + self.GetSpaces(before) + "└──── " + str(self.right.value))
            self.right.Print2(data, before + 6, index + 1)

    def ValueFixed(self):
        value = ""
        if(len(str(self.value)) < 6):
            value += self.value
            while len(value) < 6:
                value += " "
        else:
            i = 0
            while len(value) < 6:
                value += str(self.value)[i]
                i += 1
        return value

    def GetSpaces(self, count):
        value = ""
        for x in range(count):
            value += " "
        return value