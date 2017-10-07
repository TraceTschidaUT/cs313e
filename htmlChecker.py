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

class InvalidTag(Exception):

    def __init__(self, tag):
        self.tag = tag

class EmptyStack(Exception):

    def __init__(self, tag):
        self.tag = tag
    
def getTag(file):

    # read one character at a time
    char = file.read(1)
    while char != "": # end of line
        
        # check the character to see if it is a symbol starting
        if char == "<":

            # read the next characters until there is a > or while space
            tag = "" # holds the tag string
            char = file.read(1)
            while char != ">" and (not char.isspace()):
                
                # add the chars to a string
                tag += char

                # go to the next char
                char = file.read(1)

            # add the tag to the list
            # return the string
            return (tag, char)
            
            # exit the loop
            break

        # go to the next character
        char = file.read(1)

def main():

    # stack for tags
    tagStack = Stack()

    # exception tags
    EXCEPTIONS = ["br", "meta", "hr"]

    # valid tags
    VALIDTAGS = []

    # hold all of the tags returned
    tags = []

    try: # until there is an end of line error

        # open the file and begin reading it
        with open('htmlfile.txt', 'r') as f:

            # loop through each line and call get tag
            while True:

                # call get tag
                tag, char = getTag(f)

                # append the tag
                tags.append(tag)

                # check to see if end of line
                if char == "":
                    break
    except:

        # reached end of line 
        print("Finished readeding tags now comparing \n")

    # iterate through the list and find match
    for tag in tags:

        try: 
            # check if opening tag
            if tag[0] != "/":
                
                # check to see if the tag is an exception 
                if tag in EXCEPTIONS:

                    # print the results
                    print("Tag " + tag + " does not need to match: stack is still " + str(tagStack))
                    continue # skip to the next tag

                # push the tag to the stack and print the results
                tagStack.push(tag)

                # check to see if the tag is in the valid tags
                # add the tag if not
                if tag not in VALIDTAGS:

                    # add the tag to VALIDTAGS
                    VALIDTAGS.append(tag)
                    print("New tag " + tag + " found and added to list of vavlid tags")

                print("Tag " + tag + " push: stack is now " + str(tagStack))
            
            else: # check to see if closing tag matches

                # check to see if the stack has any more elements
                if not tagStack.isEmpty():

                    if tag[1:] == tagStack.peek():

                        # remove the top of the stack
                        tagStack.pop()
                        print("Tag " + tag + " matches top of stack: stack is now " + str(tagStack))
                    
                    else: 
                        # the tag does not match the tag
                        raise InvalidTag(tag)

                else: # the stack is empty

                    # raise empty stack error
                    raise EmptyStack(tag)

        except InvalidTag as it:

            # print therror message and continue
            print("Error: tag is " + it.tag + " but top of stack is " + tagStack.peek())
            quit()
        
        except EmptyStack as es:
            
            # print that there were too many closing tags
            print("Error: stack is empty but remaing closing tags")
            quit()
    
    
    # print the results
    if tagStack.isEmpty():
        print("Processing complete. No mismatches found")
    else:
        print("Processing complete. Unmatched tag remain on stack " + str(tagStack))

    # print Valid Tags
    print("VALIDTAGS:")
    print(VALIDTAGS)

    # print the exceptions
    print("EXCEPTIONS:")
    print(EXCEPTIONS)

main( ) 