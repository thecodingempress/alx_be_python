pattern_size = int(input("Enter the size of the pattern: "))
y = pattern_size
while pattern_size == y:
    for i in range(1, pattern_size + 1):
        print(f"*" * pattern_size)
    pattern_size -= 1