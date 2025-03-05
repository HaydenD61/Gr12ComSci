# Lesson 29

def consonantCheck(text, vowel=False):
    ''' determines number of consonants in a word

    '''
    
    counter = 0

    for character in text:
        character = character.lower()
        if character.isalpha() and character not in {'a', 'e', 'i', 'o', 'u'}:
            counter += 1
    
    if not vowel:
        return counter
    else:
        # return len(text) - counter
        counter = 0

        for character in text:
            character = character.lower()
            if character.isalpha() and character in {'a', 'e', 'i', 'o', 'u'}:
                counter += 1
        return counter


print(f'the count is: {consonantCheck("Hello World!")}')
print(f'the count is: {consonantCheck("Hello World!", True)}')