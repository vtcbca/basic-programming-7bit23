def reverse_string_for_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Enter a string: ")
reversed_string = reverse_string_for_loop(string)
print(f"Reversed string: {reversed_string}")
