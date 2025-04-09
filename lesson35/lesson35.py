# Lesson 35

def removeDuplicates(aList):
    """Remove duplicates from a list."""
    newList = []
    for item in aList:
        if item not in newList:
            newList.append(item)
    return newList

aList = [1, 1, 1, 2, 2, 3, 4, 5, 3, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", aList)
bList = removeDuplicates(aList)
print("List with duplicates removed:", bList)