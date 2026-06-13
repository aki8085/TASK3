# Pattern 1 - Increasing stars
print("Pattern 1:")
for i in range(1, 6):
    print("*" * i)

# Pattern 2 - Decreasing stars
print("\nPattern 2:")
for i in range(5, 0, -1):
    print("*" * i)

# Pattern 3 - Number triangle
print("\nPattern 3:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()