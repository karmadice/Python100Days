print("Enter any number to find an average of it:")
number = int(input())
startPoint = 0
totalSum = 0    # initialize the variable to be used in loop
# loop from startPoint to given number
for num in range(1, number + 1, 1):
    totalSum = startPoint + totalSum + num
print(f"Sum of first {number} numbers is: {totalSum}")
average = totalSum / number
print(f"Average of {number} number is: { average }")