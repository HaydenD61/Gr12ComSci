# Lesson 5
# Get input
startCash = input("Enter the starting cash here: ")
startCash = float(startCash)
cookies = input("Enter the cookies sold here (bcbcbc...): ")
totalSold = cookies.count("b") + cookies.count("c")
bigCookie = cookies.count("b")
smallCookie = cookies.count("c")

# calculating profits
bCost = float(bigCookie * 0.75)
cCost = float(smallCookie * 0.50)
totalCost = float(bCost + cCost)

bMoney = float(bigCookie * 2.00)
cMoney = float(smallCookie * 1.25)
totalMoney = float(bMoney + cMoney)

totalProfit = float(totalMoney - totalCost)
endCash = float(startCash + totalProfit)


# Output
print(f"Total cookies sold: {totalSold}, Total profit: {totalProfit}, current balance: {endCash}")