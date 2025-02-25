# Lesson 12

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
sum = sum([angle1, angle2, angle3])


if sum != 180:
    print("The angles do not form a triangle.")
else:
    if angle1 == angle2 == angle3:
        print("The triangle is equilateral.")
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")


