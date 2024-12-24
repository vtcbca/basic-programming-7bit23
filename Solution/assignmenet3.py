def fibonacci_recursive(n, sequence=[0, 1]):
    if len(sequence) >= n:
        return sequence[:n]
    else:
        sequence.append(sequence[-1] + sequence[-2])
        return fibonacci_recursive(n, sequence)

terms = int(input("Enter the number of terms: "))
fib_seq = fibonacci_recursive(terms)
print(f"Fibonacci sequence with {terms} terms: {fib_seq}")
