import math

# Read the number of terms to generate
n = int(input("Enter the number of Fibonacci terms: "))

# First two Fibonacci numbers
t1 = 1
t2 = 1
result = 0

# Loop from 1 to n
for i in range(1, n + 1):
    # Print the current term (t1)
    print(t1, end=" ")

    # Calculate the next term in the sequence
    result = t1 + t2

    # Shift the sequence forward
    t1 = t2
    t2 = result
