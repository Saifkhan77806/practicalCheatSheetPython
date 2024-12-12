def factorial(num):
    if(num == 1):
        return 1

    return num * factorial(num - 1)
# Test the recursive function
number = 5
number = int(input("enter num"))
print(f"The factorial of {number} is: {factorial(number)}")

