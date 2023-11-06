# Francisco Sanchez
# 11/5/23

import math

# Get user input for the value for which you want to calculate the factorial
n = int(input("Enter a non-negative integer: "))

# Initialize a variable to store the factorial using a for loop
factorial_result = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    factorial_result *= i

# Calculate the factorial using the math.factorial function
factorial_from_math_module = math.factorial(n)

# Print the results
print(f"Factorial (using for loop): {factorial_result}")
print(f"Factorial (using math.factorial): {factorial_from_math_module}")