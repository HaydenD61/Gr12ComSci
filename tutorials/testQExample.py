from random import choice

while True:
    cpu = choice(["r", "p", "s"])
    p = input("Enter rps: ")
    if p == cpu:
        print("tie")
    elif p == "r" and cpu == "s" or p == "s" and cpu == "p" or p == "p" and cpu == "r":
        print("win")
    else: 
        print("lose")

    if input("Do you want to play again? (y/n): ") == "n":
        print("Goodbye!")
        break


