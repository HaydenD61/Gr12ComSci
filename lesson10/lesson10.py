# Lesson 10

num = [input("Enter last 4 digits of phone number: ")]

i = 0
if num[i] == 8 or num[i] == 9:
    i += 1
    if num [i] == num [i + 1]:
        i += 2
        if num [i] == 8 or num [i] == 9:
            print("Number is a scammer.")
else:
    print("Number is not a scammer.")