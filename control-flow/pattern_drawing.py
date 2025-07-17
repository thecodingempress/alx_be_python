pattern_size = int(input("Enter the size of the pattern: "))
y = 0
while y < pattern_size:
    for i in range(1, pattern_size + 1):
        print("*", end="")
    print()
    y += 1