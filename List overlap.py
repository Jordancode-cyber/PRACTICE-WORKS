#This program returns an overlap of lists between numbers.

def list_overlap(list1, list2):
    return list(set(list1) & set(list2))

# Real-time example
print("Common number elements are:", list_overlap([1, 2, 3, 4], [3, 4, 5, 6]))


#This program returns an overlap of lists.

def list_overlap(list1, list2):
    return list(set(list1) and set(list2))

#Output
print("This list returns an overlapping list:", list_overlap([1,2,4,5,6,7,8,9,0], [1,7,5,0]))