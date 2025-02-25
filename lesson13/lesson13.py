# Lesson 13

inputDate = input("Enter a date (MM DD): ")


if inputDate[0] == "02" and inputDate[1] == "18":
    print("Special")
elif inputDate < "02 18":
    print("Before")
else:
    print("After")
