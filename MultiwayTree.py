#  File: MultiwayTree.py
#  Description: determines if two multi way trees are isometric 
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 12/1/2017
#  Date Last Modified: 12/1/2017

class Stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class MultiwayTree():
  
    def __init__(self, pyTree):

        if pyTree != "":
            self.data = None
            self.children = []

            # create a new stack to the hold the parens
            s = Stack()
            s.push(pyTree[0])
            del pyTree[0]

            while not s.isEmpty():

                # add the remaining nodes
                self.addChildren(pyTree, self.children, s)

    def addChildTree(self):
        pass

    # helper to add a tree recusively      
    def addChildren(self, pyTree, children, s):

        # while loop until hit a number        
        # get the first charcter
        char = pyTree[0]
        
      
        # check to see if starting a new list
        if char == "[":

            char_after = pyTree[1]

            # if the next char is a closed paren
            # means there are no more children
            if char_after == "]":
                
                # remove the [
                del pyTree[0]
                del pyTree[1] 
                return 
            
            # if the char after is not a symbol them it is a child
            elif char_after.isalnum():
                
                # add the data value to the class and recure
                children.append(MultiwayTree(pyTree))
                # s.pop()
                # self.data = char_after
                # del pyTree[0]
                # self.addChildren(pyTree, children, s)
            
            # a new tree is being made
            elif char_after == "[":
                
                # create a new tree

                # push onto the the stack b/c did not go through init
                # only way this if state works is if called from a data point previously
                # need to add to the stack so it can close later 
                s.push(pyTree[0])
                del pyTree[0]
                children.append(MultiwayTree(pyTree))

        # if the char is a data value
        elif char.isalnum():
            self.data = char
            del pyTree[0]
            self.addChildren(pyTree, children, s)
        
        # if done with child
        elif char == "]":
            s.pop()
            del pyTree[0]
            return

        # If comma or space
        else:
            del pyTree[0]
            self.addChildren(pyTree, children, s)


    def preOrder(self): 
        print(self.data, end=" ")
        if self.children != []:
            for child in self.children:
                child.preOrder()

    def isIsomorpicTo(self, otherTree):
        pass

    def insertChild(self, newTree):
        pass

def cleanTreeFile(tree_line_1):
    tree_list_1 = []
    idx = 0
    while idx < len(tree_line_1):
        if tree_line_1[idx].isspace() or tree_line_1[idx] == "," or tree_line_1[idx] == '"':
            idx += 1
            continue
        else:
            ch = tree_line_1[idx]
            if tree_line_1[idx].isalnum() and idx < len(tree_line_1):
                if tree_line_1[idx + 1].isalnum():
                    ch +=  tree_line_1[idx + 1]
                    idx += 1
            tree_list_1.append(ch)
            idx +=1
    return tree_list_1

def main():
    with open("MultiwayTreeInput.txt") as f:
      
        # read the first line and remove the endings
        tree_line_1 = f.readline().strip()
        
        # print the first line
        print(tree_line_1)

        # clean the tree
        tree_list_1 = cleanTreeFile(tree_line_1)

        # build the first multi tree
        tree_1 = MultiwayTree(tree_list_1)

        tree_1.preOrder()
        print()

        # read the second line and remove the endings
        tree_line_2 = f.readline().strip()

        # print the second line
        print(tree_line_2)

        # clean the tree line from the file
        tree_list_2 = cleanTreeFile(tree_line_2)

        # build the second multi tree
        tree_2 = MultiwayTree(tree_list_2)

        tree_2.preOrder()
        print()


main()