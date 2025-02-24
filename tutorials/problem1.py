#perfect number check?

num = int(input("enter a number: "))
total = 0
divider = 1
while divider < num:
    if num % divider == 0:
        total += divider
    
    divider += 1

# end of while
if total == num:
    print("perfect number")
elif total < num:
    print("deficient number")
else:
    print("abundant number")
