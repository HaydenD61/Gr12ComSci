# Lesson 21

num = int(input("Enter a number: "))
factors = set()

for i in range(1, num + 1):
    factors1 = set()
    for j in range(1, i):
        if num % j == 0:
            factors.add(j)
    factors.add(len(factors1))

largest = (factors)
print(f"The number with the most factors is {largest}")

