# Francisco Sanchez
# 11/5/23

import random
import math

# Number of random points to generate
num_points = 1000000

# Initialize counters for points inside the circle
inside_circle = 0

# Generate random points and check if they are inside the circle
for _ in range(num_points):
    x = random.uniform(0, 1)  # Random x-coordinate between 0 and 1
    y = random.uniform(0, 1)  # Random y-coordinate between 0 and 1
    distance = math.sqrt(x**2 + y**2)  # Distance from the origin
    if distance <= 1:
        inside_circle += 1

# Calculate the approximation of pi
pi_approximation = 4 * inside_circle / num_points

print("Approximation of pi:", pi_approximation)
print("Value of math.pi:", math.pi)