# Lesson 31

def anaCheck(word1, word2):

    aList = list(word1)
    bList = list(word2)

    if word1 == word2:
        word = "ANAGRAM!"
    elif len(aList) == len(bList):
        for i in aList:
            if i in bList:
                bList.remove(i)
        if len(bList) == 0:
            word = "ANAGRAM!"
    else:
        word = "NOT AN ANAGRAM!!"  

    return word

word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")
print(anaCheck(word1, word2))