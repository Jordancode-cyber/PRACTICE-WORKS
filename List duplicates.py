#This program removes duplicates within lists.

def remove_duplicates(lst):
    return list(set(lst))

#Output

print("List without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5, 7, 9]))
