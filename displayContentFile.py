def displayFileContent(fileName):
   try:       
    with open(fileName, "r") as file:
        content = file.read()
        print(content)
   except FileNotFoundError:
      print("file not found")
  

# path = input("enter path of the file:- ")

path = input("Enter path of the file:-")


str = path.replace("\\", "\\\\")



displayFileContent(str)
