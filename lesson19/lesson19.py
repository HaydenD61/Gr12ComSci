# Lesson 19

num = int(input("Enter a number: "))
i = 1

for i in range(1, num + 1):
    if num % i == 0 and i != 1 and i != num:
        print(f"{num} is not a prime number")
        break
    elif num % i > 0 or i == num:
        print(f"{num} is a prime number")
        break

