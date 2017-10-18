#  File: ERsim.py
#  Description: An ER simulator using queues
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 10/14/2017
#  Date Last Modified: 10/17/2017

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):

        # loop through backwards to change the queue order for printing
        i = len(self.items) - 1
        strQueue = [] # queues printed
        while i >= 0:
            strQueue.append(self.items[i])

            i -= 1

        return(str(strQueue))

def main():

    # create the queues
    criticalQueue = Queue()
    seriousQueue = Queue()
    fairQueue = Queue()

    # create a loop to accept commands
    # open the file of commands
    with open("ERsim.txt", "r") as f:

        quit = False

        for line in f:

            # get out of the loop, command exit
            if quit:
                break

            # get the command
            command = line.strip()

            # splits the command into its parts
            command_components = command.split(" ")

            # determine the command type
            if command_components[0] == "add":

                # determine the queue
                if command_components[1] == "Critical":
                    addPatient(command_components[2], criticalQueue, "Critical")
                
                elif command_components[1] == "Serious":
                    addPatient(command_components[2], seriousQueue, "Serious")
                
                elif command_components[1] == "Fair":
                    addPatient(command_components[2], fairQueue, "Fair")

                # print the updated queues
                printQueues(fairQueue, seriousQueue, criticalQueue)

            elif command_components[0] == "treat":

                # check if treating next or condition
                if command_components[1] == "next":

                    treated = treatNext(command_components, fairQueue, seriousQueue, criticalQueue)
                    
                    if treated:
                        # print the updated queues
                        printQueues(fairQueue, seriousQueue, criticalQueue)

                elif command_components[1] == "all":
                    treatAll(fairQueue, seriousQueue, criticalQueue)

                else:
                    condition = command_components[1] # get the condition
                    is_empty = True # variable to know if print

                    if condition == "Critical":
                        is_empty = treatCondition(condition, criticalQueue)
                    
                    elif condition == "Serious":
                        is_empty = treatCondition(condition, seriousQueue)
                   
                    elif condition == "Fair":
                        is_empty = treatCondition(condition, fairQueue)
                    
                    if not is_empty:
                        # print the updated queues
                        printQueues(fairQueue, seriousQueue, criticalQueue)

            elif command_components[0] == "exit":
                print("Command: Exit\n")
                quit = True

def addPatient(patient, queue, typeQueue):
    
    # add the patient to the queue
    queue.enqueue(patient)

    # print the command
    print("Command: Add patient " + patient + " to " + typeQueue + " queue\n")

    
def treatNext(commands, fair, serious, critical):

    # know if patients left
    treated = False

    # treat the next patient
    print("Command: Treat next patient\n")

    # check the queues in order of seriousness
    if not critical.isEmpty():

        # dequeue the patient 
        patient = critical.dequeue()

        # print the results
        print("\tTreating '" + patient + "' from Critical queue")
        treated = True

    elif not serious.isEmpty():

        # dequeue the patient 
        patient = serious.dequeue()

        # print the results
        print("\tTreating '" + patient + "' from Serious queue")
        treated = True

    elif not fair.isEmpty():
        
        # dequeue the patient 
        patient = fair.dequeue()

        # print the results
        print("\tTreating '" + patient + "' from Fair queue")
        treated = True

    else:
        print("\tNo patient in queues\n")  

    return treated 

def treatAll(fair, serious, critical):

    # print the command
    print("\nCommand: Treat all patients\n")

    # loop through each queue and print the results
    while not critical.isEmpty():
        patient = critical.dequeue()
        print("\n\tTreating '" + patient + "' from Critical queue")
        printQueues(fair, serious, critical)
    
    while not serious.isEmpty():
        patient = serious.dequeue()
        print("\n\tTreating '" + patient + "' from Serious queue")
        printQueues(fair, serious, critical)
    
    while not fair.isEmpty():
        patient = fair.dequeue()
        print("\n\tTreating '" + patient + "' from Fair queue")
        printQueues(fair, serious, critical)
    
    print("\n\tNo patients in queues\n")

def treatCondition(condition, queue):
    
    # print the command
    print("Command: Treat next patient on " + condition + " queue \n")

    if not queue.isEmpty():

        # get the patient 
        patient = queue.dequeue()
        print("\tTreating '" + patient + "' from " + condition + " queue")

        # return queue is not empty
        return False
    else:
        print("\tNo patients in queue\n")
        return True


def exitErSim():

    print("Command: Exit \n")
    exit()

def printQueues(fair, serious, critical):

    print("\tQueues are:")
    print("\tFair:     " + str(fair))
    print("\tSerious:  " + str(serious))
    print("\tCritical: " + str(critical))
    print()

# call the main function 
main()
