str = "this is structured is developed by saif khan"
list1 = set(str)

print("This will so the show how many each character is present in the string")

for i in list1:
    if(i != " "):
        print(f"{i} is present in this string {str.count(i)} times.")
        


