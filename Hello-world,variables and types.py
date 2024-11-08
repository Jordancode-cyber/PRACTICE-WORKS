print("This line will be printed")
x=1
if x==1:
    #indented four spaces
    print("x is 1")
    
print("Hello, World!")

my_int=7
print(my_int)
my_float = 7.0
print(my_float)
my_float = float(7)
print(my_float)

my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)

my_string = "Don't worry about apostrophes"
print(my_string)

one = 1
two = 2
three = one + two
print(three)

hello = 'hello'
world = "world"
hello_world = hello + " " + world
print(hello_world)

a, b = 3, 4
print(a, b)

#This will not work at all!
one = 1
two = 2
hello = 'hello'

#Editable code
my_string = 'hello'
my_float = 10.0
my_int = 20
# code testing
if my_string == 'hello':
    print("string: %s" %my_string)
if isinstance(my_float, float) and my_float == 10.0:
    print("float: %f" % my_float)
if isinstance(my_int, int) and my_int == 20:
    print("integer: %d "%my_int)