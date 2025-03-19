# Lesson 32

def letter(word1, word2):

    aList = list(word1)
    bList = list(word2)
    shared = []

    if word1 == word2:
        shared = list(word1)
    else:
        for i in aList:
            if i in bList:
                shared.append(i)
    
    return sorted(shared)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
print(letter(word1, word2))