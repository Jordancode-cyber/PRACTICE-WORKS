#This function counts vowels within a text.

def count_vowels(s):
    vowels = "a,e,o,u,i"
    return sum(1 for char in s.lower() if char in vowels)

print(count_vowels("My name is Feta Jordan"))
#It will count the number of vowels in any text given.
#Vowels = 7, Text = My name is Feta Jordan