#CCC painting tutorial

userInput = [int(x) for x in input().split()] #input is a string, so we need to convert it to a list of integers
w1, h1, w2, h2, = userInput

if h1 > h2:
    ht = h1
else:
    ht = h2

wt = w1 + w2

perim = (2 * ht) + (2 * wt)

print(perim)
