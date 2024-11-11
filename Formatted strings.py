# A function that returns a formatted string
#Method 1

def greeting():
    name = "Alice"
    age = 30
    
print(f"Hello, my name is {"Alice"} and I am {30} years old.")


#Method 2

def greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


print(greeting("Alice", 30))
# Output: "Hello, my name is Alice and I am 30 years old."