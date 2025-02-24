# inputting string with @
user_input = input("Enter string with @: ")

# finding @ & outputting index
i = 0

if len(user_input) == 0:
    print("No @ found.")
elif len(user_input) == 1:
    if user_input == "@":
        print("Found @ at index 0.")
    else:
        print("No @ found.")
elif len(user_input) > 1:
    while i < len(user_input):
        if user_input[i] == "@":
            print(f"Found @ at index {i}.")
            #break
        i += 1
    # end of while loop
else:
    print("No @ found.")
