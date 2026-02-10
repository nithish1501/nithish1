# The "Old" Way
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# The Intermediate Way (List Comprehension)
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary Comprehension
# Creating a mapping of numbers to their cubes
cube_map = {x: x**3 for x in range(5)}

print(squares)  # [0, 4, 16, 36, 64]
print(cube_map) # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}