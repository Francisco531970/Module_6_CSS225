# Francisco Sanchez
# 11/5/23

import math

# Get user input for radians
radians = float(input("Enter a value in radians: "))

# Convert radians to degrees using the formula
degrees_conversion = radians * (180 / math.pi)

# Use the math.degrees function to convert radians to degrees
degrees_from_math_module = math.degrees(radians)

print(f"Converted value (using formula): {degrees_conversion} degrees")
print(f"Converted value (using math.degrees): {degrees_from_math_module} degrees")