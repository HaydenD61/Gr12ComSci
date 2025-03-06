# Lesson 30

def pattern (ptrn):
    ''' takes input and creates pattern of 1 and 0 corresponding with the length inputted.

    Args:
        ptrn - requires an integer input to determine length of pattern

    Returns:
        list of 1 and 0 in corresponding pattern to input
    '''

    pat = []
    i = 0
    while i < ptrn:
        if i % 2 == 0:
            pat.append(1)
        else:
            pat.append(0)
        i += 1

    return pat


print(pattern(int(input("Enter Number: "))))
