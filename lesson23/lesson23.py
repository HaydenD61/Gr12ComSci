# Lesson 23

numbers = set()

while True:
    num = (input("Enter a number/done when done: "))
    if num == "done":
        break
    else:
        numbers.add(int(num))

average = sum(numbers) // len(numbers)
print(f"The average of the numbers is {average}")