num = int(input("enter a positive integer: "))
while num % 2 == 0:
    print(2)
    num = num // 2

if num > 1:
    divider = 3
    while num != 1:
        if num % divider == 0:
            print(divider)
            num = num // divider 
        else:
            divider += 2
    
