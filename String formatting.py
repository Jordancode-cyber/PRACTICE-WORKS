#Python uses C-style string formatting to create new, formatted strings. 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list)
#Together with a format string, which contains normal text together with "argument specifiers", 
#special symbols like "%s" and "%d".

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
print("Hello, " f"{name}!")

#To use two or more argument specifiers, we use a tuple (parentheses)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#or we can use formatted strings for easier understanding and reference
name = "John"
age = 23
print(f"{name} is {age} years old.")

#Any object which is not a string can be formatted using the %s operator as well
#This prints out: A list: [1,2,3]
my_list = [1,2,3]
print("A list: %s" %my_list)


# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


#Exercise
#write a format string which prints out the data using the following syntax: 
#Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)