# Lesson 17

num = int(input("Enter a number: "))
factorial = 1

while num > 0:
    factorial = factorial * num
    num -= 1

print(factorial)
