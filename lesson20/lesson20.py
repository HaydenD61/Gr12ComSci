# Lesson 20


for i in range(1, 10000):
    factors = set()
    for n in range(1, i + 1):
        while n < i:
            if i % n == 0:
                factors.add(i)
                n += 1
            
        if sum(factors) == i:
            print(f"{i} is a perfect number")




        
