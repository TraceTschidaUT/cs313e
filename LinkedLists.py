#  File: LinkedLists.py
#  Description: Demo of ordered and unorder linked list
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/20/2017
#  Date Last Modified: 10/22/2017

class Node (object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None            # always do this saves a lot
                                  # of headaches later!
    def getData (self):
        return self.data            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

    def setNext (self,newNext):
        self.next = newNext         # changes a POINTER

class LinkedList():

    def __init__(self):
        self.head = None

    def __str__ (self):
        # Return a string representation of data suitable for printing.
        #    Long lists (more than 10 elements long) should be neatly
        #    printed with 10 elements to a line, two spaces between
        #    elements
        dataList = []

        # Return the number of items in the list 

        currentNode = self.head # pointer to the first node

        while currentNode != None:
            dataList.append(currentNode.getData())
            currentNode = currentNode.getNext()

        count = 0
        string = ""
        for i in dataList:

            if count % 10 == 0 and count != 0:
                string += "\n"
            
            string += (str(i) + "  ")

            count += 1
        # return the number of items
        return string

  
    def addFirst (self, item): 

        # Add an item to the beginning of the list
        tempNode = Node(item) # creates a new node
        tempNode.setNext(self.head) # sets the nodes next to the current heads pointer
        self.head = tempNode # sets the head to the new node

    def addLast (self, item): 
        # Add an item to the end of a list
        
        # create a new node 
        newNode = Node(item)

        # traverse the list until you get to the end 
        if self.head == None: # no items in the linked list
            self.addFirst(item)

        else:

            currentNode = self.head

            while True:

                # check to see if the next node is none
                # then you have reached the end 
                if currentNode.getNext() == None:

                    # point the current last node to the new one
                    currentNode.setNext(newNode) # passes the pointer
                    break

                else: # if there is a pointer to another node

                    # advance the current node
                    currentNode = currentNode.getNext()


    def addInOrder (self, item): 
        # Insert an item into the proper place of an ordered list.
        # This assumes that the original list is already properly
        # ordered.

        # traverse the list until you get to the end 
        currentNode = self.head # pointer to the first node
        newNode = Node(item) # creat a new node to be inserted 
        inserted = False

        if self.head == None: # first item
            self.addFirst(item)
            inserted = True

        elif currentNode.getNext() == None: # add second item
            
            if currentNode.getData() > item:
                newNode.setNext(currentNode)
                self.head = newNode
            else:
                currentNode.setNext(newNode)

            inserted = True             
        
        else: # all other items

            # compare the nodes until current node is bigger 
            # and previous node is less than or equal to
            previousNode = currentNode
            currentNode = currentNode.getNext()

            while not inserted:

                # if it is the largest node becuase no more are left
                if newNode.getData() >= currentNode.getData() and currentNode.getNext() == None: # only possible if last node
                    
                    currentNode.setNext(newNode)
                    inserted = True

                # only possible if the smallest node
                elif newNode.getData() < previousNode.getData():

                    newNode.setNext(previousNode)
                    self.head = newNode

                    inserted = True

                elif newNode.getData() < currentNode.getData() and newNode.getData() >= previousNode.getData():

                    # insert inbetween previous and current nodes
                    newNode.setNext(currentNode)
                    previousNode.setNext(newNode)

                    inserted = True
                
                else:

                    # advance the nodes
                    previousNode = currentNode
                    currentNode = currentNode.getNext()
                
                    

    def getLength (self):
        # Return the number of items in the list 

        currentNode = self.head # pointer to the first node
        count = 0 # number of items in list

        while currentNode != None:
            currentNode = currentNode.getNext()
            count += 1
        
        # return the number of items
        return count
     
    def findUnordered (self, item): 
        # Search in an unordered list
        # Return True if the item is in the list, False
        # otherwise.

        found = False
        currentNode = self.head
        
        while currentNode != None and not found:

            # see if the data matches the current item
            if currentNode.getData() == item:
                found = True

            else: # advance currentNode to the next in the list
                currentNode = currentNode.getNext() # changes the pointer
        
        return found

    def findOrdered (self, item): 
        # Search in an ordered list
        # Return True if the item is in the list, False
        # otherwise.
        # This method MUST take advantage of the fact that the
        # list is ordered to return quicker if the item is not
        # in the list.

        found = False
        currentNode = self.head # may need to see if head has data first
            
        while currentNode != None and not found and currentNode.getData() <= item:

            # see if the data matches the current item
            if currentNode.getData() == item:
                found = True

            else: # advance currentNode to the next in the list
                currentNode = currentNode.getNext() # changes the pointer
        
        return found

    def delete (self, item):
        # Delete an item from an unordered list
        # if found, return True; otherwise, return False

        found = False
        currentNode = self.head
        previousNode = None
        
        while currentNode != None and not found:

            # see if the data matches the current item
            if currentNode.getData() == item:
                
                # need to check where the item is 
                # if it is the first item change the head
                if previousNode == None:
                    self.head = currentNode.getNext()

                else: # if the node is in the middle or end
                    previousNode.setNext(currentNode.getNext())

                found = True

            else: # advance currentNode to the next in the list
                
                previousNode = currentNode # sets the pointer
                currentNode = currentNode.getNext() # changes the pointer
        
        return found

    def copyList (self):
        # Return a new linked list that's a copy of the original,
        # made up of copies of the original elements

        # create a blank linked list
        newList = LinkedList()

        currentNode = self.head # first node in the list

        while currentNode != None: # no more pointers

            # get the next node and add it the list
            newList.addLast(currentNode.getData())
            currentNode = currentNode.getNext()

        # return the list
        return newList

    def reverseList (self): 
        # Return a new linked list that contains the elements of the
        # original list in the reverse order.

        # create a blank linked list
        newList = LinkedList()

        currentNode = self.head # first node in the list

        while currentNode != None: # no more pointers

            # get the next node and add it the list
            newList.addFirst(currentNode.getData())
            currentNode = currentNode.getNext()

        # return the list
        return newList

    def orderList (self): 
        # Return a new linked list that contains the elements of the
        # original list arranged in ascending (alphabetical) order.
        # Do NOT use a sort function:  do this by iteratively
        # traversing the first list and then inserting copies of
        # each item into the correct place in the new list.

        # create a blank linked list
        newList = LinkedList()

        currentNode = self.head # first node in the list

        # add the newnode to the new linked list
        newList.addFirst(currentNode.getData()) # make a new node with same data
        currentNode = currentNode.getNext()

        while currentNode != None: # no more pointers

            # get the next node and add it the list
            newList.addInOrder(currentNode.getData())
            currentNode = currentNode.getNext()
            

        # return the list
        return newList

    def isOrdered (self):
        # Return True if a list is ordered in ascending (alphabetical)
        # order, or False otherwise

        currentNode = self.head # first node in the list
        previousNode = None # does not point to anything
        ordered = True
        singleNode = False

        # return true for only one node
        if self.getLength() < 2:
            singleNode = True 
        else: # move previous and current 1 node up
            previousNode = currentNode
            currentNode = currentNode.getNext()     

        while currentNode != None and ordered and not singleNode: # no more pointers

            # check to see if the current is greater than previous
            if currentNode.getData() >= previousNode.getData():
                
                # go up 1 node
                previousNode = currentNode
                currentNode = currentNode.getNext()
            else: # current < previous
                ordered = False

        # return if the list is in order
        return ordered

    def isEmpty (self): 
        # Return True if a list is empty, or False otherwise
        return (self.head == None)

    def mergeList (self, b): 
        # Return an ordered list whose elements consist of the 
        # elements of two ordered lists combined.

        # create a blank linked list
        newList = LinkedList()

        # get the starting nodes for boths linked lists
        a_currentNode = self.head # pointer to the first value
        b_currentNode = b.head # pointer to the first value

        # loop through each list until 1 of them has no more nodes
        while a_currentNode != None and b_currentNode != None: # no more pointers

            # determine which value is larger
            # add that to the new list 
            # advance that list 1 node
            if a_currentNode.getData() <= b_currentNode.getData():

                # create a new node and add it
                newList.addLast(a_currentNode.getData())

                # advance a list 1 node 
                a_currentNode = a_currentNode.getNext()
            
            else:

                # create a new node and add it
                newList.addLast(b_currentNode.getData())

                # advance a list 1 node 
                b_currentNode = b_currentNode.getNext()
        
        while a_currentNode != None:
            
            # add the remaining a linked list elements
            newList.addLast(a_currentNode.getData())

            # move to the next node
            a_currentNode = a_currentNode.getNext()

        while b_currentNode != None:
            # create a new node and add it
            newList.addLast(b_currentNode.getData())

            # advance a list 1 node 
            b_currentNode = b_currentNode.getNext()
            

        # return the list
        return newList

    def isEqual (self, b):
        # Test if two lists are equal, item by item, and return True.

        # get the first nodes in lists
        a_currentNode = self.head
        b_currentNode = b.head
        equal = True

        while equal and a_currentNode != None and b_currentNode != None:

            if a_currentNode.getData() == b_currentNode.getData():

                # advance both current nodes to the next node in the lists
                a_currentNode = a_currentNode.getNext()
                b_currentNode = b_currentNode.getNext()

            else:
                equal = False
        
        return (equal and (a_currentNode == None and b_currentNode == None))

    def removeDuplicates (self):
        # Remove all duplicates from a list, returning a new list.
        # Do not change the order of the remaining elements.

        # get the first node
        currentNodePointer = self.head
        previousNodePointer = None
        newList = LinkedList()
        empty = False

        # list of elements in the linked lists
        dataList = []

        # special case with no elements
        if self.isEmpty():
            empty = True # return an empty new list
        
        while currentNodePointer != None and not empty: # end of list
            
            if (currentNodePointer.getData() in dataList):

                # do not add a new node
                # incase the next one is also in the list
                currentNodePointer = currentNodePointer.getNext()
            
            else: # node is not a duplicate 

                # add the current node data value to the 
                # list of all values
                data = currentNodePointer.getData()
                dataList.append(data)

                # add the value to a new node
                # add the new node to the linked list
                newList.addLast(data)

                # move the current node pointers up a node
                currentNodePointer = currentNodePointer.getNext()
                

        return newList


# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
