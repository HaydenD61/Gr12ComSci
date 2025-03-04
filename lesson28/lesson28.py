# Lesson 28

word = input("Enter word: ")

if word[0] != word[-1]:
    print("Not a palindrome!")
else:
    word1 = word[:: -1]
    if word == word1:
        print("Palindrome!!")
    else:
        print("NOT A PALINDROME!!")

