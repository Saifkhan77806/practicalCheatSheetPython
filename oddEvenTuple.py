tuple1 = (1,3,5,7,9,3,7,80)

print(tuple1)

for i in tuple1:
    if(i%2==0):
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")