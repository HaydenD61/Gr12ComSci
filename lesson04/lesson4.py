# Lesson 4
import math

fences = input("Enter amount of fence planks for section 1 here(FFF):" )
fences2 = input("Enter amount of fence planks for section 2 here(FFF):" )
fences3 = input("Enter amount of fence planks for section 3 here(FFF):" )

fences = len(fences)
fences2 = len(fences2)
fences3 = len(fences3)
total = fences + fences2 + fences3

paint = (math.ceil(total / 12))
paint2 = (math.ceil(total % 12))

cost = paint * 14.95

print(f"You will need {total} buckets of paint, which will cost you ${cost}. You will have {paint2} buckets of paint left over.")