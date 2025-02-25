# dusas and yobis

dusaSize = int(input("Enter size of the Dusa: "))

while True:
    yobiSize = int(input("Enter size of the Yobi: "))
    if yobiSize >= dusaSize:
        print("Dusa got scared and ran away")
        break
    else:
        dusaSize += yobiSize
        print(f"Dusa is now {dusaSize} units tall")

print(f"Dusa finsihed at {dusaSize} units tall")