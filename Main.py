import random
import Node
from BinaryTree import BinaryTree

def Main():
    print("Hello World")

#Main()
bin1 = BinaryTree()

#bin1.Add(235)
#bin1.Add(153)
#bin1.Add(124)
#bin1.Add(115)
#bin1.Add(89)
#bin1.Add(364)
#bin1.Add(546)

for x in range(50):
    bin1.Add(random.randint(0, 1000))

bin1.display()

#print([0, 1, 2, 3, 4] * 2)
