# Lesson 11

input = input("Enter x and y coordinates: ")
input = input.split()
x = int(input[0])
y = int(input[1])

if y > 0 and x > 0:
    print(f"Point ({x}, {y}) is in Quadrant I.")
elif y > 0 and x < 0:
    print(f"Point ({x}, {y}) is in Quadrant II.")
elif y < 0 and x < 0:
    print(f"Point ({x}, {y}) is in Quadrant III.")
else:
    print(f"Point ({x} {y}) is in Quadrant IV.")
