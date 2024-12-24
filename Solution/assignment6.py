def print_pattern_nested_for_loop(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

rows = int(input("Enter the number of rows: "))
print_pattern_nested_for_loop(rows)
