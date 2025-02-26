# problem9
# shorter Way using lists
# num = input("Enter a number: ")
# amount = 0

# while len(num) > 1:
    # num = [int(i) for i in num]
    # num = str(num)
    # print(num)
    # amount += 1

# print(f"it took {amount} iterations to get to a single digit number")

## longer way without using lists
num = int(input("Enter a number: "))
strNum = str(num)
steps = 0
while len(strNum) > 1:
    i = 0
    total = 0
    while i < len(strNum):
        total += int(strNum[i])
        i += 1
    steps += 1
    strNum = str(total)
print(f"It took {steps} iterations to get to a single digit number")