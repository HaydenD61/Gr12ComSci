# Lesson 37

def compress(word):
    compressed = ''
    count = 1

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
        else: 
            compressed += word[i] + str(count)
            count = 1
        
    compressed += word[-1] + str(count)
    return compressed

print(compress(input('Enter Word Here: ')))
        
        
