def f(word):
    if len(word) == 0:
        return None
    if len(word) == 1:
        return word
    else:
        return f(word[1:]) + word[0]

# Faster due to no slicing
def f2(word, i=-1, result=''):
    if len(word) <= 1:
        return word
    elif len(word)*(-1) == i:
        return result + word[i]
    else:
        return f2(word, i-1, result + word[i])

word = input("Enter a word: ")
print(f(word))
print(f2(word))