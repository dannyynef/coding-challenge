
# For the reverseString function, originally I wrote it to use a for loop iterating through and changing the string.
# However in python strings are immutable, so to make it more efficient I changed it to a list, modified the list, and then converted it back into a string when returning. 
# This took it from O(n^2) to O(n) time complexity.
def reverseString(string):
    # Convert the string to a list of characters
    chars = list(string)
    left = 0
    right = len(chars) - 1
    # Use a while loop to swap characters from the ends towards the center
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    # Returning and converting the list back to a string
    return ''.join(chars)


# This approach here is fairly straightforward and is O(1) time complexity. It simply initiates the first number as the largest and then checks to see if the other numbers are bigger.
def largestNumber(num1, num2, num3):
    largest = num1

    if num2 > largest:
        largest = num2

    if num3 > largest:
        largest = num3

    return largest


# Also fairly straightforward approach that uses O(n) complexity
def calculateFactorial(num):
    # Check to ensure it is possible to find the factorial of the number
    if num < 0:
        return "Not possible, factorial must be greater than or equal to 0"

    # Creates a for loop that iterates up to how big the number is starting at 0. Multiplies the running total to whatever number iteration it is on.
    factorial = 1
    for i in range(1, num+1):
        factorial *= i

    return factorial


# This approach uses O(n) time complexity and is fairly simple.
def calculateFibSeq(n):
    # Ensures we are using a number that can be calculated.
    if n <= 0:
        return "Not possible, n must be greater than 0"

    # Establishes initial variables
    a = 0
    b = 1

    # Replaces a with b and then replaces b with the sum of a and b. Which follows the Fibonacci sequence, meaning once the for loop ends a will be the result.
    for i in range(n):
        a, b = b, a + b

    return a


# Personal tests to ensure functionality
# result = reverseString("hello")
# print(result)

# result = largestNumber(1, 5, 3)
# print(result)

# result = calculateFactorial(0)
# print(result)

# result = calculateFibSeq(6)
# print(result)
