my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0]) #prints 1
print(my_list[1]) #prints 2
print(my_list[2]) #prints 3

#prints out 1,2,3
for x in my_list:
    print(x)
    
my_list =[1,2,3,4,5,6,7,8,9,10]
print(my_list[5])
#you can't print an index of a value which does not exist

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)