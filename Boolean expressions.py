#This function will return a True for any person over 18 years(an adult)

def is_adult(age):
    return age >= 18

print(is_adult(20))
# Output: True

print(is_adult(16))
# Output: False

#Method 2

age = 18
is_adult = True
if is_adult:
    print("This person is above the age of 18.")
else:
    print("This person is below the age of 18.")
    
