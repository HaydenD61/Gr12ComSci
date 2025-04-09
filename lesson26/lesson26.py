# Lesson 26

def factorCount(number):
    ''' determines number of factors a number has

    Args:
        number: an integer needed to determine the number of its factors
    
    Returns:
        an integer, which is the total amount of factors from 1 to N 
    '''
    counter = 0
    for divider in range(1, number+1):
        if number % divider == 0:
            counter +=1
    
    return counter

upperLimit = int(input("Enter N: "))

for num in range(1, upperLimit+1):
    factorSize = factorCount(num)

    print(f"{num} has {factorSize} factors.")