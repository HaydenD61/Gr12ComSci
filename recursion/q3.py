def f(word):
    if len(word) == 0:
        return False
    elif len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return f(word[1:-1])
        else:
            return False
word = input("Enter a word: ")
print(f(word))