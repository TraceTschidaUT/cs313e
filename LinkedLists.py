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
        previousNode = None # no pointer becuase nothing before at first
        newNode = Node(item) # creat a new node to be inserted 
        inserted = False

        # compare the nodes until current node is bigger 
        # and previous node is less than or equal to
        while not inserted:

            # if the current node is smaller then need to advance
            # the current node to the next node 
            if currentNode.getData() <= newNode.getData() and currentNode.getNext() != None:
                
                # advance previous then current nodes 1 node
                previousNode = currentNode # set the pointer
                currentNode = currentNode.getNext() # sets the pointer
            
            # you have found the location
            # greater than or equal to previous
            # less than current
            else if previousNode.getData() <= newNode.getData() and currentNode.getData() > newNode.getData():

                # new node needs to point to current
                newNode.setNext(currentNode)

                # previous needs to point to the new node
                previousNode.setNext(newNode)

                # current is already pointing the the next node
                inserted = True

            # if it is the largest node
            else if currentNode.getData() < newNode.getData() and currentNode.getNext() == None:

                # the new node is the last node
                # change the current node's pointer
                currentNode.setNext(newNode)

                inserted = True
            
            # if the node is the smallest
            else if currentNode.getData() > newNode.getData() and previousNode == None:

                # change the head to point to the new node
                newNode.setNext(currentNode)
                self.head = newNode

                inserted = True
                

    def getLength (self):
        # Return the number of items in the list 

        currentNode = self.head # pointer to the first node
        count = 0 # number of items in list

        while currentNode != None:
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
                    self.head == currentNode.getNext()

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
        newNode = Node(currentNode.getData()) # make a new node with same data

        # add the newnode to the new linked list
        newList.addFirst(newNode)

        while currentNode != None: # no more pointers

            # get the next node and add it the list
            currentNode = currentNode.getNext()
            newList.addFirst(Node(currentNode.getData()))

        # return the list
        return newList

    def reverseList (self): 
        # Return a new linked list that contains the elements of the
        # original list in the reverse order.

        # create a blank linked list
        newList = LinkedList()

        currentNode = self.head # first node in the list
        newNode = Node(currentNode.getData()) # make a new node with same data

        # add the newnode to the new linked list
        newList.addFirst(newNode)

        while currentNode != None: # no more pointers

            # get the next node and add it the list
            currentNode = currentNode.getNext()
            newList.addLast(Node(currentNode.getData()))

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
        newNode = Node(currentNode.getData()) # make a new node with same data

        # add the newnode to the new linked list
        newList.addFirst(newNode)

        while currentNode != None: # no more pointers

            # get the next node and add it the list
            currentNode = currentNode.getNext()
            newList.addInOrder(Node(currentNode.getData()))

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
            if a_currentNode.getData() >= b_currentNode.getData():

                # create a new node and add it
                newList.addLast(Node(a_currentNode.getData()))

                # advance a list 1 node 
                a_currentNode = a_currentNode.getNext()
            
            else:

                # create a new node and add it
                newList.addLast(Node(b_currentNode.getData()))

                # advance a list 1 node 
                b_currentNode = b_currentNode.getNext()
        
        while a_currentNode != None:
            
            # add the remaining a linked list elements
            newList.addLast(Node(a_currentNode.getData()))

            # move to the next node
            a_currentNode = a_currentNode.getNext()

        while b_currentNode != None:
            # create a new node and add it
            newList.addLast(Node(b_currentNode.getData()))

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
                newNode = Node(data)
                newList.addLast(newNode)

                # move the current node pointers up a node
                currentNodePointer = currentNodePointer.getNext()
                

        return newList
