# problem 2: outputing individual words in list

sentence = input("Enter a sentence: ")

# easy way
# words = sentence.split()
# for word in words:
#     print(word)

word = ""
i = 0
while i < len(sentence):
    if sentence[i] == " ":
        print(word)
        word = ""
    else:
        word += sentence[i]

    i += 1
# end of while loop
if word and word != " ":
    print(word)
