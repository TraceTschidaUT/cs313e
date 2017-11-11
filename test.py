def trace(a,b):
    a = 1
    b.append(4)

def main():

    z = 2
    y = [4,5]

    trace(z, y)

    print(z,y)

main()