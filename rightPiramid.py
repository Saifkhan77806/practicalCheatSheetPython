def printl(str):
    print(str, end=" ")

for i in range(1, 6):
    num = 2 ** (i - 1)  # Calculate the starting number for the current row
    for x in range(i):
        printl(num)
        num //= 2  # Divide by 2 to get the next number in the row
        
    print("\n")