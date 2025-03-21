# Lesson 39

def gcf(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    factors1 = []
    for i in range(1, num1):
        if num1 % i == 0:
            factors1.append(i)
    
    factors2 = []
    for i in range(1, num2):
        if num2 % i == 0:
            factors2.append(i)
    
    common = []
    for i in factors1:
        if factors1[i] in factors2:
            common.append(i)
    
    return max(common)

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
print(gcf(num1, num2))