def is_palindrome_for_loop(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

string = input("Enter a string: ")
if is_palindrome_for_loop(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
