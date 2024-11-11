#This function will give us the lengths of each word in a sentence we type

def word_lengths(sentence):
    words = sentence.split()
    return{word: len(word) for word in words}


print(word_lengths("Please input your sentence here"))