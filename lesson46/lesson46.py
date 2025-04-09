# Lesson 46

def nextValue(num):
    if num % 2 == 0:
        return num // 2
    else:
        return(3 * num) + 1

def sequenceMaker(start, table):
    if start in table:
        return table[start]
    else:
        sequence = [start]
        size = 1

        while sequence[-1] != 1 and sequence[-1] not in table:
            newNum = nextValue(sequence[-1])

            if newNum in table:
                size = size + table[newNum]
                break
            else:
                sequence.append(newNum)
                size += 1
        
        for i in range(len(sequence)):
            table[sequence[i]] = size - i

        return size
    
memory = {1:1, 2:2}

start = 13
test = sequenceMaker(start, memory)

print(f"{start} has a sequence of {test} numbers")
print()
for key, value in memory.items():
    print(f"{key} has {value} terms")
print()

memory = {1:1, 2:2}

for start in range(3, 10000000):
    currentLength = sequenceMaker(start, memory)


answer = 0
longestLength = 0
for key in range(1, 10000000):
    if memory[key] > longestLength:
        answer = key
        longestLength = memory[key]

print(f"The longest sequence is {longestLength} and starts with {answer}")