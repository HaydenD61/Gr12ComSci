# Lesson 33

def mean(nums):
    
    avrg = sum(nums) // len(nums)

    return avrg

def median(nums):

    ordered = sorted(nums)
    mid = (len(ordered) // 2) - 1

    return (ordered[mid])


nums = []
while True:
    inpt = input("Enter number: ")
    if inpt.lower() == 'x':
        break
    else:
        nums.append(int(inpt))

print(f"Mean: {mean(nums)}")
print(f"Median: {median(nums)}")

