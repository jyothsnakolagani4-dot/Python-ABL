"""
Case Study 5: Advanced Numeric Pattern Generator
Generate a hollow diamond using nested loops and validate the requested size.
"""

print("ADVANCED NUMERIC PATTERN GENERATOR")
print("----------------------------------")

while True:
    try:
        size = int(input("Enter diamond size (1-9): "))
        if 1 <= size <= 9:
            break
        print("Invalid size. Enter a number from 1 to 9.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Upper half, including the middle row
for row in range(1, size + 1):
    print(" " * (size - row), end="")
    if row == 1:
        print(row)
    else:
        print(str(row) + " " * (2 * row - 3) + str(row))

# Lower half, excluding the middle row
for row in range(size - 1, 0, -1):
    print(" " * (size - row), end="")
    if row == 1:
        print(row)
    else:
        print(str(row) + " " * (2 * row - 3) + str(row))

print("Pattern generated successfully.")