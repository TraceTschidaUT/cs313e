def main():

    a = [1,2,3]
    b = a 

    b[1] = 9

    print(a,b)
main()


class stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    