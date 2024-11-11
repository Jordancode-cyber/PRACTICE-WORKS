#This function will return the square of all even numbers from 1 to n.

def even_numbers(n):
    return[
        x ** 2 for x in range(1, n + 1)
        if x % 2 == 0]
    
print(even_numbers(10))