# StringCleaner

text = input("Enter an uncleaned string: ")
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
cleanText = []
for char in text:
    if char in alphabet:
        cleanText.append(char)

word = "".join(cleanText)
print(word)