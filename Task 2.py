from typing import List

LengthOfList = 10


########################## Hashing algorithm (Task 2.3(
def hashing(id):
    firstpart = ""
    for i in range(2):
        char = str(ord(id[i]))
        firstpart = (firstpart + char)
    for i in range(2, 6):
        char = id[i]
        firstpart = (firstpart + char)
    hash = int(firstpart)
    return (hash - 65650000) % LengthOfList


########################### Code for Creating Binary tree

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

        print("Index position:", i, self.data),
        if self.right:
            self.right.PrintTree()

    # findval method to compare the value with nodes
    def findval(self,lkpval):  #Task(2.5)
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return False
            return self.right.findval(lkpval)
        else:
            return True
    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root): #Task(2.5)
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)

        return res



#####################################
##########    ID generator Task(2.4)
def ID_Generator():
    import random
    # index_for_search_val = random.randint(0, LengthOfList)           ######## to test if search function works
    IdGenArr = []
    for r in range(LengthOfList):
        a = str(chr(random.randint(65, 90)))
        b = str(chr(random.randint(65, 90)))
        c = str(random.randint(65, 90))
        d = str(random.randint(65, 90))
        e = str(random.randint(65, 90))
        f = str(random.randint(65, 90))

        if r == 0:  ######## to test if search function works
            global SearchVal
            SearchVal = a + b + c + d + e + f
            IdGenArr.append(SearchVal)

        if r != 0:
            IdGenArr.append(a + b + c + d + e + f)  ######## to test if search function works

    return IdGenArr


############# Calling ID generator Task(2.4)

IdGenArr = ID_Generator()

############################### Innitialise array
Array = [""] * LengthOfList
for r in range(LengthOfList):
    Array[r] = Node(0)

################################# Data Input

for r in range(LengthOfList):
    data = IdGenArr[r]
    index = hashing(data)
    Array[index].insert(data)

for i in range(LengthOfList): #Task(2.5)
    print("Index no:",i,":",Array[i].inorderTraversal( Array[i]))
#
#for i in range(LengthOfList): #Task(2.5)
#   print(Array[i].inorderTraversal( Array[i]))
#
#
#
print("the search value is ", SearchVal)
searchIndex = hashing(SearchVal)

if Array[searchIndex].findval(SearchVal):
    print("The ",SearchVal," is in index no:",searchIndex)

