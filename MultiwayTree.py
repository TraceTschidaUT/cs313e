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

      # set the instance variables to none
      self.data = None
      self.children = []
      
      # get the first value
      first_val = pyTree[1]

      self.data = first_val
      
      # build the python tree with lists with a stack
      s = Stack()
      
      # build a tree node
      
      self.addLoop(pyTree, )

    # helper to add a tree recusively      
    def addLoop(self, pyTree, multiTree):
      
        # check to see if starting a new list
        if char == "[":
            
            
        # check to see if closing
        elif char = "]":
            s.pop()

        # check to see if
        else:
            pass

    def preOrder(self):
        pass

    def isIsomorpicTo(self, otherTree):
        pass

    def insertChild(self, newTree):
        pass
  
def main():
    with open("MultiwayTreeInput.txt") as f:
      
        # read the first line and remove the endings
        tree_line_1 = f.readline().strip()
        
        # print the first line
        print(tree_line_1)

        # read the second line and remove the endings
        tree_line_2 = f.readline().strip()