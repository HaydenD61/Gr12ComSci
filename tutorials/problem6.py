# problem 6

num = int(input("Enter a number greater than 1: "))

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3) + 1
    print(num)

