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


def main():

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.setNext(node2)
    node2.setNext(node3)

    head = node3.getNext() # head is the pointer to next node
    print(head.getData()) # accessing the data through the point
    print(head)

main()

else if (self.getLength() == 1):
            newList.addFirst(currentNodePointer.getData())

        else if self.getLength() == 2:

            # create the previous node pointer 
            previousNodePointer = currentNodePointer

            # move the current to the 2nd node
            currentNodePointer = currentNodePointer.getNext()

            if currentNodePointer.getData() == previousNodePointer.getData():
                newList.addFirst(Node(currentNodePointer.getData()))

            else if currentNodePointer.getData() > previousNodePointer.getData():
                
                newList.addFirst(Node(currentNodePointer.getData()))
                newList.addFirst(Node(previousNodePointer.getData()))
        else:
            previousNodePointer = currentNodePointer
            currentNodePointer = currentNodePointer.getNext()

            # add the first element to the new list 
            newList.addFirst(Node(previousNodePointer.getData()))
            dataList.append(previousNodePointer.getData())