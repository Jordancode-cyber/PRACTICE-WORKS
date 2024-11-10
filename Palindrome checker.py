#The "palindrome_function" checks if a given string is a palindrome, ignoring case and punctuation.

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Real-time example
print("Is 'Radar' a palindrome?", is_palindrome("Radar"))
print("Is 'Hello' a palindrome?", is_palindrome("Hello"))
