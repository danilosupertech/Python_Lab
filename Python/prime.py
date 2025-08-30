def prime(n):
    i: int = 2
    count: int = 0

    if n <= 1:
        return False

    while i <= n:
        if (n % i == 0 and i < n):
            count += 1

        i += 1

    return count == 0


# Initialize a variable to store the sum of all prime numbers below 100
prime_sum = 0

# Loop through all numbers from 2 to 99
for i in range(2, 100):
    # Check if i is prime using the prime function
    if prime(i):
        # If i is prime, add it to the prime_sum variable
        prime_sum += i

# Print the sum of all prime numbers below 100
print(prime_sum)
