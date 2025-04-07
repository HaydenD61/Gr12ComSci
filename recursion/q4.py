def f(word):
    if len(word) == 0:
        return None
    if len(word) == 1:
        return word
    else:
        return f(word[1:]) + word[0]
word = input("Enter a word: ")
print(f(word))