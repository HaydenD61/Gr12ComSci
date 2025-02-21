# Lesson 8

winCount = 0
for _ in range(6):
    currentResult = input(f"Enter result of game {_ + 1} here (W/L): ")

    if currentResult == "W":
        winCount += 1
# end of for loop

group = 0
if winCount > 4:
    group = 1
elif winCount > 2:
    group = 2
elif winCount > 0:
    group = 3

if group == 0:
    print("Player is eliminated")
else:
    print(f"Player is in group {group}")



