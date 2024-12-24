def print_triangle_nested_loop(n):
    for i in range(1, n + 1):
        row = " " * (n - i)  # Add leading spaces
        for j in range(1, 2 * i):
            row += str(j) + " "  # Concatenate numbers
        print(row.strip())  # Strip trailing spaces before printing

n = int(input("Enter the number of rows: "))
print_triangle_nested_loop(n)
