

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

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2

            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, oldWidth, oldHeight, oldMiddle = self.left._display_aux()

            line = '%s' % self.value
            width = len(line)

            first_line = (oldMiddle + 1) * ' ' + (oldWidth - oldMiddle - 1) * '_' + line
            second_line = oldMiddle * ' ' + '/' + (oldWidth - oldMiddle - 1 + width) * ' '

            shifted_lines = []
            for line in lines:
                shifted_lines.append(line + width * ' ')

            newLines = [first_line, second_line] + shifted_lines

            return newLines, oldWidth + width, oldHeight + 2, oldWidth + width // 2

        # Only right child.
        if self.left is None:
            lines, oldWidth, oldHeight, oldMiddle = self.right._display_aux()

            line = '%s' % self.value
            width = len(line)

            first_line = line + oldMiddle * '_' + (oldWidth - oldMiddle) * ' '
            second_line = (width + oldMiddle) * ' ' + '\\' + (oldWidth - oldMiddle - 1) * ' '

            shifted_lines = []
            for line in lines:
                shifted_lines.append(width * ' ' + line)

            newLines = [first_line, second_line] + shifted_lines

            return newLines, oldWidth + width, oldHeight + 2, width // 2

        # Two children.
        left, oldWidthLeft, oldHeightLeft, oldMiddleLeft = self.left._display_aux()
        right, oldWidthRight, oldHeightRight, oldMiddleRight = self.right._display_aux()

        line = '%s' % self.value
        width = len(line)

        first_line = (oldMiddleLeft + 1) * ' ' + (oldWidthLeft - oldMiddleLeft - 1) * '_' + line + oldMiddleRight * '_' + (oldWidthRight - oldMiddleRight) * ' '
        second_line = oldMiddleLeft * ' ' + '/' + (oldWidthLeft - oldMiddleLeft - 1 + width + oldMiddleRight) * ' ' + '\\' + (oldWidthRight - oldMiddleRight - 1) * ' '

        if oldHeightLeft < oldHeightRight:
            left += [oldWidthLeft * ' '] * (oldHeightRight - oldHeightLeft)
        elif oldHeightRight < oldHeightLeft:
            right += [oldWidthRight * ' '] * (oldHeightLeft - oldHeightRight)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + width * ' ' + b for a, b in zipped_lines]

        return lines, oldWidthLeft + oldWidthRight + width, max(oldHeightLeft, oldHeightRight) + 2, oldWidthLeft + width // 2

