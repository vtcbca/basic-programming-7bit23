def print_pattern_nested_for_loop(n):
    for i in range(1, n + 1):
        row = " " * (n - i)  # Add leading spaces
        
        # Add increasing characters
        for j in range(1, i + 1):
            row += chr(64 + j) + " "
        
        # Add decreasing characters
        for j in range(i - 1, 0, -1):
            row += chr(64 + j) + " "
        
        print(row.strip())  # Strip trailing spaces before printing

n = int(input("Enter the number of rows: "))
print_pattern_nested_for_loop(n)
