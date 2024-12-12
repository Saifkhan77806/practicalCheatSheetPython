def printl(str):
    print(str,end=" ")


for i in range(1,6):
    for x in range(6 - i, 0, -1):
        printl(x)
    print("\n")
    