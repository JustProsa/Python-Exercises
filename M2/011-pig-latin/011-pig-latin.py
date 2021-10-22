# Pig Latin is a language constructed by transforming English words.
# While the origins of the language are unknown, it is mentioned in at least two documents from the nineteenth century,
# suggesting that it has existed for more than 100 years. The following rules are used to translate English into Pig Latin:

# If the word begins with a consonant (includingy),
# then all letters at the beginning of the word, up to the first vowel (excluding y),
# are removed and then added to the end of the word, followed by ay.
# For example, computer becomes omputercay and think becomes inkthay.

# If the word begins with a vowel (not including y), then way is added to the end of the word.
# For example, algorithm becomes algorithmway and office becomes officeway.

# Write a program that reads a line of text from the user.
# Then your program should translate the line into Pig Latin and display the result.
# You may assume that the string entered by the user only contains lowercase letters and spaces.

print("\nEnter your string to translate it in Pig Latin")
user_input = input()

def pigLatin(strn):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    L = strn.split()
    for word in L:
        word = list(word)
        for e in word:
            if e in consonants:
                counter = 0
                while word[counter] in consonants:
                    word.append(word[counter])
                    word.remove(word[counter])
                    counter += 1
                word.append("ay")
            elif e in vowels:
                word.append("way")
        word = "".join(list(word))
    L = " ".join(L)
    
    return L
    


print(pigLatin(user_input))

# vowels = ["a", "e", "i", "o", "u"]
# consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# L = user_input.split()
# for word in L:
#     if list(word)[0] in consonants:
#         for e in list(word):
#             if e in consonants:
#                 list(word).append(e)
#                 list(word).remove(e)
#         list(word).append("way")
#     elif list(word)[0] in vowels:
#         list(word).append("way")
#     "".join(list(word))
#     print(word, end= " ")
