list1 = [1,2,3,5,62,6,3,7,6,4,7,9,2,1,62,3]

# To remove duplication from the list
nonDuplicatedList = set(list1)
nonDuplicatedList = list(nonDuplicatedList)


print(f"List with duplication {list1}")
print(f"List without duplication {nonDuplicatedList}")