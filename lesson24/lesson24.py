# Lesson 24

names = []
while True:
    name = input("Enter a name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    names.append(name)

large = names[0]
for i in names:
    if i > large:
        large = i

print("The largest name is:", large)