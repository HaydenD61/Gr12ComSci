# Lesson 18

num = int(input("Enter a number: "))
factors = set()

for i in range(1, num + 1):
    if num % i == 0:
        factors.add(i)
        
print(f"{factors} are the factors of {num}")
