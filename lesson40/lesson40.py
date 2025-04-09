# Lesson 40

def prime(num):
    
    primes = []
    for i in range (1, num):
        if i % 2 > 0:
            if i % 3 > 0:
                primes.append(i)
    return primes

num = int(input('Enter number here: '))
print(prime(num))
        