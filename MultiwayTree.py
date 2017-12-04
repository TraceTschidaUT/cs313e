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

        same = True
        
        # check to see if the number of children at this level are the same
        if len(self.children) == len(otherTree.children):

            # loop through the remaining children and determine if they are the same
            # if there are no more children 
            # return true becuase at the end
            # base case
            if self.children == []:
                return True

            # else there are more children for both
            else:

                # move through each of the children to see if thir children are the same nubers
                child_idx = 0
                while child_idx < len(self.children):

                    # determine if their children are the same
                    same = self.children[child_idx].isIsomorpicTo(otherTree.children[child_idx])

                    # if the number of children are not the same break out and return false
                    if same == False:
                        return same
                    else:
                        # move to the next child
                        child_idx += 1
        
        # else, the children are not the same number
        else:
            # return false becuase not iso morphic
            # base case
            return False

        return same
    


    def insertChild(self, newTree):
        pass

def cleanTreeFile(tree_line_1):

    # create a list of the elements of the string
    # makes iterating when building the tree easier
    tree_list_1 = []

    # counter to move through the string
    idx = 0
    while idx < len(tree_line_1):

        # skip over spaces, commas, and quotation marks
        if tree_line_1[idx].isspace() or tree_line_1[idx] == "," or tree_line_1[idx] == '"':
            idx += 1
            continue
        else:

            # build a string with the element's parts
            ch = tree_line_1[idx]

            # if the element is more than 1 character long
            # add the next element and increase the index
            if tree_line_1[idx].isalnum() and idx < len(tree_line_1):
                if tree_line_1[idx + 1].isalnum():
                    ch +=  tree_line_1[idx + 1]
                    idx += 1
            
            # append the full element to the tree
            # increase index and continue
            tree_list_1.append(ch)
            idx +=1

    # return the list of elements
    return tree_list_1

def main():
    with open("MultiwayTreeInput.txt") as f:

        tree_count = 1

        while True:
      
            # read the first line and remove the endings
            tree_line_1 = f.readline().strip()

            if not tree_line_1:
                break
            
            # print the first line
            print("Tree 1: ", tree_line_1)

            # clean the tree
            tree_list_1 = cleanTreeFile(tree_line_1)

            # build the first multi tree
            tree_1 = MultiwayTree(tree_list_1)

            # print the tree in preOrder
            print("Tree {:} preorder: ".format(tree_count), end="  ")
            tree_1.preOrder()
            print()
            print()

            # increment the tree counter
            tree_count += 1

            # read the second line and remove the endings
            tree_line_2 = f.readline().strip()

            # print the second line
            print("Tree 2:", tree_line_2)

            # clean the tree line from the file
            tree_list_2 = cleanTreeFile(tree_line_2)

            # build the second multi tree
            tree_2 = MultiwayTree(tree_list_2)

            # print in preorder
            print("Tree {:} preorder:".format(tree_count), end="   ")
            tree_2.preOrder()
            print()
            print()

            answer = tree_1.isIsomorpicTo(tree_2)

            if answer:
                print("Tree {:} is isomorphic to Tree {:}".format(tree_count - 1, tree_count))
            else:
                print("Tree {:} is not isomorphic to Tree {:}".format(tree_count - 1, tree_count))

            # print spacing
            print()
            print()

            # incrememnt the tree counter
            tree_count += 1


main()