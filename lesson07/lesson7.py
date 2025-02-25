# Lesson 7
from random import randrange


dc = int(input("Enter the DC level: "))
dice = randrange(1, 20)

if dice >= dc:
    print(f"You rolled a {dice} and passed the DC")
else:
    print(f"You rolled a {dice} and failed the DC")


