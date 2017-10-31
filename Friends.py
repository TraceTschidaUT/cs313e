#  File: Friends.py
#  Description: Social media friends feature with linked lists implementation
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/31/2017
#  Date Last Modified: 10/31/2017

class Node ():
    
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

class UnorderedList ():

    def __init__(self):
        sentinel = Node(None)
        self.head = sentinel

    def isEmpty (self):
        return self.head.getNext() == None

    def add (self, _user):
        # add a new Node to the beginning of an existing list
        temp = Node(_user)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def length (self):
        current = self.head.getNext()
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search (self, _user):

        current = self.head.getNext()
        found = False

        while current != None and not found:
            if current.getData().name == _user.name:
                found = True
            else:
                current = current.getNext()

        return found

    def remove (self, _user):
        current = self.head.getNext()
        previous = self.head
        found = False

        while not found:

            if current.getData().name == _user.name:
                found = True
            else:
                previous = current
                current = current.getNext()

        previous.setNext(current.getNext())

    def getNode (self, _user):

        # get the first friend
        currentPointer = self.head.getNext()
        found = False

        # loop through each node
        while currentPointer != None and not found:

            if (currentPointer.getData().name == _user.name):

                # set found to true and end looping
                found = True

            # else advance the current pointer to the next node
            else:
                currentPointer = currentPointer.getNext()

        # return the pointer to the friend
        return (currentPointer)

class User():

    def __init__(self, _name):
        self.name = _name
        self.friends = UnorderedList()

    def __str__(self):

        # get the first friend
        # b/c sentenial have to move the first real node
        currentPointer = self.friends.head.getNext()

        # string to hold the friends
        friends = "[ "

        # loop through until the pointer is none
        while currentPointer != None:

            # add to the friends string
            friends += currentPointer.getData().name + " "

            # move to the next pointer
            currentPointer = currentPointer.getNext()

        # end the string
        friends += "]"

        return (friends)

    def addFriend(self, _user):

        # add the friend to the first user
        self.friends.add(_user)

        # add the friend to the second user
        _user.friends.add(self)

    def deleteFriend(self, _user):

        # remove the friend from the first user
        self.friends.remove(_user)

        # remove the friend from the second user
        _user.friends.remove(self)

    def queryFriend(self, _user):

        # return if user is in the friends list
        return (self.friends.search(_user))

def main():

    # create the users linked list
    usersLinkedList = UnorderedList()

    # open the commands while
    with open("FriendData.txt", "r") as f:

        # loop through each command
        for line in f:

            # strip the line endings away
            command = line.strip().split(" ")

            # parse the command

            # command Person
            # create a new person
            if (command[0] == "Person"):

                # create a new person
                person = User(command[1])

                # check to see if the person is in the list already
                if not usersLinkedList.search(person):

                    # add the person to the list of users
                    usersLinkedList.add(person)

                    # print the output message
                    print(command[1] + " now has an acocunt.")

                else:

                    # print error message
                    print("A person with name " + command[1] + " already exists.")

            elif (command[0] == "Friend"):

                friend1 = User(command[1])
                friend2 = User(command[2])

                # find the users
                foundFriend1 = usersLinkedList.search(friend1)
                foundFriend2 = usersLinkedList.search(friend2)

                # if the same user
                if (friend1.name == friend2.name):

                    print("A person cannot friend him/herself.")
                
                # if the users exist and are separate
                elif foundFriend1 and foundFriend2:

                    # add the friends to both
                    # get the pointer for the user
                    user1Pointer = usersLinkedList.getNode(friend1).getData()
                    user2Pointer = usersLinkedList.getNode(friend2).getData()

                    # check to see if they are already friends
                    if (user1Pointer.queryFriend(user2Pointer)):

                        print(friend1.name + " and " + friend2.name + " are already friends.")
                    
                    # if they are not already friends
                    # make them friends
                    else:

                        # make them friends
                        user1Pointer.addFriend(user2Pointer)

                        # print the output
                        print(friend1.name + " " + friend2.name + " are now friends.")

                else:

                    # print messages for users who do not exist
                    if not foundFriend1:
                        print("A person with name " + friend1.name + " does not currently exist.")

                    if not foundFriend2:
                        print("A person with name " + friend2.name + " does not currently exist.")

            elif (command[0] == "Unfriend"):

                # create two temporary users
                friend1 = User(command[1])
                friend2 = User(command[2])

                # find the users
                foundFriend1 = usersLinkedList.search(friend1)
                foundFriend2 = usersLinkedList.search(friend2)

                # check to see if it is the same person 
                if (friend1.name == friend2.name):
                    print("A person cannot friend him/herself.")
                
                # check to see the users exist
                elif (foundFriend1 and foundFriend2):

                    # get the two users
                    # get the pointer for the user
                    user1Pointer = usersLinkedList.getNode(friend1).getData()
                    user2Pointer = usersLinkedList.getNode(friend2).getData()

                    # check to see if not friends
                    if (not user1Pointer.queryFriend(user2Pointer)):

                        # print the error message
                        print("{:} and {:} aren't friends, so you can't unfriend them.".format(friend1.name, friend2.name))
                    
                    # if they are friends then remove break the friendship
                    else:

                        # break the friendship
                        user1Pointer.deleteFriend(user2Pointer)

                        # print the output
                        print("{:} and {:} are no longer friends.".format(friend1.name, friend2.name))

                # if the users do not exist
                else:
                    
                    # print messages for users who do not exist
                    if not foundFriend1:
                        print("A person with name " + friend1.name + " does not currently exist.")

                    if not foundFriend2:
                        print("A person with name " + friend2.name + " does not currently exist.")

            # list all friends
            elif (command[0] == "List"):

                # create a temporary user 
                # see if the exist in linked list
                friend1 = User(command[1])
                foundUser = usersLinkedList.search(friend1)

                if (foundUser):

                    # get the user
                    # print the list of users
                    user1 = usersLinkedList.getNode(friend1).getData()

                    # print the list
                    print(str(user1))
                
                # if the user does not exist
                else:
                    print("{:} does not exist".format(friend1.name))

            # find if two users are friends 
            elif (command[0] == "Query"):
                
                # create 2 temporary Users
                friend1 = User(command[1])
                friend2 = User(command[2])

                # query based on name
                foundFriend1 = usersLinkedList.search(friend1)
                foundFriend2 = usersLinkedList.search(friend2)

                # if the users are found 
                if (foundFriend1 and foundFriend2):

                    # query the friends list
                    # get the user pointer
                    user1Pointer = usersLinkedList.getNode(friend1).getData()
                    user2Pointer = usersLinkedList.getNode(friend2).getData()

                    # check to see if they are friends
                    # if they are friends
                    if (user1Pointer.queryFriend(user2Pointer)):

                        print("{:} and {:} are friends.".format(friend1.name, friend2.name))

                    # if the users are not friends
                    else:

                        print("{:} and {:} are friends.".format(friend1.name, friend2.name))
                
                # if one of users is not found 
                else:
                    # print messages for users who do not exist
                    if not foundFriend1:
                        print("A person with name " + friend1.name + " does not currently exist.")

                    if not foundFriend2:
                        print("A person with name " + friend2.name + " does not currently exist.")

            # if the command is exit
            # break out of the loop
            elif (command[0] == "Exit"):

                print("Exiting...")
                break

main()
