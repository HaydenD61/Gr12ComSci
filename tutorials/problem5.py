# input

text = input("Enter encrypted text: ")
shift = int(input("Enter shift value: "))

decrypt = ""
n = 0
diff = 0
if shift == 0:
    print(text)
elif not text:
    print("No text entered")
else:
    while n < len(text):
        if text[n] != " ":
            if (ord(text[n]) + shift) < 65:
                diff = 64 % (ord(text[n]) + shift)
                decrypt += chr(90 - diff)
            elif (ord(text[n]) + shift) > 90:
                diff = (ord(text[n]) + shift) % 90
                decrypt += chr(64 + diff)
            else:
                decrypt += chr(ord(text[n]) + shift)
        else:
            decrypt += " "
        n += 1
print(decrypt)