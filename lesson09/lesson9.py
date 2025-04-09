# Lesson 9
import random

print ("Thank you for playing Rock, Paper, Scissors!")
print ("Please choose one of the following:")
print ("1. Rock")
print ("2. Paper")
print ("3. Scissors")
userInput = int(input("Enter your choice (1,2,3): "))

choices = [1, 2, 3]
compChoice = int(random.choice(choices))

if userInput == compChoice:
    print ("It's a tie!")
elif userInput ==1 and compChoice == 2 | userInput == 2 and compChoice == 3 | userInput == 3 and compChoice == 1:
    print ("Computer wins!")
else:
    print ("You win!")

print ("Thank you for playing Rock, Paper, Scissors!")

